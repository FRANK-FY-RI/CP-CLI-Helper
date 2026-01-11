import cloudscraper
from bs4 import BeautifulSoup as bs
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python3 cf_parse.py <PROBLEM_ID>")
    print("Example: python3 cf_parse.py 1803A")
    sys.exit(1)

pid = sys.argv[1].upper().strip()

# Validate problem id like 1803A, 1742F, 1900C1, etc.
m = re.fullmatch(r"(\d+)([A-Z]\d*)", pid)
if not m:
    print("❌ Invalid problem id format. Example: 1803A, 1900C1")
    sys.exit(1)

contest_id = m.group(1)
problem_id = m.group(2)

url = f"https://codeforces.com/contest/{contest_id}/problem/{problem_id}"
print("URL:", url)


scraper = cloudscraper.create_scraper()

print("Downloading....")
resp = scraper.get(url, timeout=10)
resp.raise_for_status() #crash if download failed

html = resp.text
soup = bs(html, "html.parser")

#Find all sample inputs and outputs
inputs = soup.select(".sample-test .input pre")
outputs = soup.select(".sample-test .output pre")

if len(inputs) == 0:
    print("No Sample Input found. Login needed or layout changed")
    sys.exit(1)

if len(inputs) != len(outputs) :
    print("⚠️ Warning: inputs and outputs count mismatch")

print(f"Found {len(inputs)} testcases")

def clean(text: str) -> str:
    #Codeforces uses <br> tags inside <pre>
    return text.replace("\r", "").strip() + "\n"

for i, (inp, out) in enumerate(zip(inputs, outputs), start=1):
    inp_txt = clean(inp.get_text("\n"))
    out_txt = clean(out.get_text("\n"))

    with open(f"{pid}{i}.in", "w") as f:
        f.write(inp_txt)
    with open(f"{pid}{i}.ans", "w") as f:
        f.write(out_txt)

    print(f"Saved: {pid}{i}.in, {pid}{i}.ans")

print("✅ Done.")
