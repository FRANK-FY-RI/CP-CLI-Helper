
# Competitive Programming CLI Helper

Fast CLI tool to compile, run and locally judge Codeforces solutions with sample test case parsing.

- Supported OS: Linux (tested on Ubuntu).
- Supported Platforms:
    - Codeforces
    - AtCoder

- Built and tested using GCC (g++-14)
## Features

- Downloads Input/Output from the platform
- Normalizes output (removes extra whitespace characters)
- Run on custom input (stdin)
- Works on C++ 23
- Returns exit codes: 
    - 0 = Accepted
    - 1 = Error
    - 2 = Wrong Answe
- Supports multiple test cases without early termination
- GCC optimized (-O2 / -O3)
- Simple Global CLI installation


## Installation

Install CP-Helper with the following steps:
- Step 1
First, install all the required dependencies.

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
Navigate to the directory where you downloaded the project, then run:
```bash
g++ -std=c++23 -O3 cph.cpp -o cph
sudo mkdir -p /opt/CPH
sudo cp ./*.* /opt/CPH
sudo ln -s /opt/CPH/cph /usr/local/bin/cph
```
Verify
```bash
cph --help
```
## Usage

```bash
cph cf fetch 4A
cph cf run 4A
cph cf test 4A
```
- fetch: Downloads the sample input/ output files and creates a `.cpp` solution file with the same name as the problem ID.
- run: Runs the custom input (stdin)
- test: Judges the solution against sample test cases and shows the first difference for every test case if any.

## Example

```bash
cph cf fetch 1803A
vim 1803A.cpp
cph cf test 1803A

```
## Motivation
- This project was built to automate competitive programming workflows:  
fetching problems, compiling solutions, and validating against sample tests — all from the terminal.