
# Competitive Programming CLI Helper

Fast CLI tool to compile, run and locally judge Codeforces solutions with sample test case parsing.

Supported OS: Linux (tested on Ubuntu).
## Features

- Downloads Input/Output from Codeforces
- Normalizes output (removes extra whitespace characters)
- Run on custom input (stdin)
- Works on C++ 23
- Returns exit codes: 
    - 0 = Accepted
    - 1 = Error
    - 2 = Wrong Anser
- Supports multiple test cases without early termination
- GCC optimized (-O2)
- Simple Global CLI installation


## Installation

Install CP-Helper with the following steps:
- Step 1
First, all the required dependencies.

Python3 (for scraper)
```bash
sudo apt update
sudo apt install python3
```
Install Python dependencies
```bash
pip install requests cloudscraper beautifulsoup4
```
This tool is written in C++ and requires a compiler.
```bash
sudo apt install g++-14
```
- Step 2
Global Installation (Linux)

The CLI depends on multiple files (`cf`, `run.sh`, `cf_parse.py`).  
Install them together into a fixed directory and expose only the launcher.
Make a folder in `/opt` and save the files from the repository in that folder
```bash
sudo mkdir -p /opt/CPJudge
sudo cp cf cf_parse.py run.sh /opt/CPJudge/
sudo ln -s /opt/CPJudge/cf /usr/local/bin/cf
```
Verify
```bash
cf --help
```
## Usage

```bash
cf fetch 4A
cf run 4A
cf test 4A
```
- fetch: Downloads the sample input/ output files and creates a `.cpp` solution file with the same name as the problem ID.
- run: Runs the custom input (stdin)
- test: Judges the solution against sample test cases and shows the first difference for every test case if any.

## Example

```bash
cf fetch 1803A
vim 1803A.cpp
cf test 1803A

```