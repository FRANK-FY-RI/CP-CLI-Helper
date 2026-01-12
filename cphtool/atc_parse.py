import requests
from bs4 import BeautifulSoup as bs
import sys
import re
import time
from requests.exceptions import ReadTimeout, RequestException

# -------------------------
# Argument Parsing
# -------------------------
if len(sys.argv) != 2:
    print("Usage: python3 atc_parse.py <PROBLEM_ID>")
    print("Example: python3 atc_parse.py abc350_a")
    sys.exit(1)

pid = sys.argv[1].lower().strip()

# Validate problem id like abc350_a, arc170_b, agc065_a
m = re.fullmatch(r"(abc|arc|agc)(\d+)_([a-z])", pid)
if not m:
    print("❌ Invalid problem id format.")
    print("Examples: abc350_a, arc170_b, agc065_a")
    sys.exit(1)

contest_type = m.group(1)
contest_num  = m.group(2)
problem_letter = m.group(3)

contest_id = f"{contest_type}{contest_num}"
url = f"https://atcoder.jp/contests/{contest_id}/tasks/{pid}"

print("URL:", url)

headers = {
    "User-Agent": "Mozilla/5.0"
}

# -------------------------
# Download with Retry
# -------------------------
print("Downloading....")

def fetch_with_retry(url, retries=3, timeout=20):
    for attempt in range(1, retries + 1):
        try:
            print(f"🌐 Fetch attempt {attempt}...")
            resp = requests.get(url, headers=headers, timeout=timeout)
            resp.raise_for_status()
            return resp
        except ReadTimeout:
            print("⏳ Timeout. Retrying...")
        except RequestException as e:
            print("❌ Network error:", e)
            time.sleep(2)

    print("❌ Failed to fetch problem page.")
    sys.exit(1)

resp = fetch_with_retry(url)

html = resp.text
soup = bs(html, "html.parser")

# -------------------------
# Extract Sample Inputs / Outputs
# -------------------------

def extract_by_prefix(prefix_in, prefix_out):
    ins, outs = [], []
    for h3 in soup.find_all("h3"):
        title = h3.get_text(strip=True)
        if title.startswith(prefix_in):
            pre = h3.find_next_sibling("pre")
            if pre:
                ins.append(pre)
        elif title.startswith(prefix_out):
            pre = h3.find_next_sibling("pre")
            if pre:
                outs.append(pre)
    return ins, outs

# First try English
inputs, outputs = extract_by_prefix("Sample Input", "Sample Output")

# If nothing found, fallback to Japanese
if len(inputs) == 0:
    inputs, outputs = extract_by_prefix("入力例", "出力例")

if len(inputs) == 0:
    print("❌ No sample inputs found.")
    sys.exit(1)

if len(inputs) != len(outputs):
    print("⚠️ Warning: input/output count mismatch")

tcases = min(len(inputs), len(outputs))
print(f"Found {tcases} testcases")

# -------------------------
# Save Files
# -------------------------
def clean(text: str) -> str:
    return text.replace("\r", "").strip() + "\n"

for i in range(tcases):
    inp_txt = clean(inputs[i].get_text())
    out_txt = clean(outputs[i].get_text())

    with open(f"{pid}{i+1}.in", "w") as f:
        f.write(inp_txt)

    with open(f"{pid}{i+1}.ans", "w") as f:
        f.write(out_txt)

    print(f"Saved: {pid}{i+1}.in, {pid}{i+1}.ans")

print("✅ Done.")
