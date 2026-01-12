#!/bin/bash

set -e

if [ "$#" -lt 3 ]; then 
    echo "Usage: ./run.sh <solution_file> <input_file> <output_file>"
    exit 1
fi

SOL="$1"
INP="$2"
ANS="$3"
OUT="out.ans"

#echo "Compiling...."
g++ -std=c++23 -O2 "$SOL" -o sol

#echo "Running...."
./sol <"$INP" > "$OUT"

#echo "Judging...."

normalize() {
    tr -d '\r' < "$1" |      # remove CR
    sed 's/[ \t]*$//' |      # trim trailing spaces
    awk 'NF'                 # remove empty lines
}

NOUT="$OUT.norm"
NANS="$ANS.norm"

normalize "$OUT" > "$NOUT"
normalize "$ANS" > "$NANS"

if diff -q "$NOUT" "$NANS" > /dev/null; then
    echo -e "\e[32m✔ Accepted\e[0m"
    rm -f "$NOUT" "$NANS"
else 
    echo -e "\e[31m✘ Wrong Answer\e[0m"
    echo "----Diff (normalized) ----"
    diff "$NOUT" "$NANS"
    rm -f "$NOUT" "$NANS"
    exit 2;
fi

