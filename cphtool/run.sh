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
BIN="sol"

if [ ! -f $BIN ] || [ "$SOL" -nt $BIN ]; then
    #echo "Compiling...."
    g++ -std=c++23 -O2 "$SOL" -o $BIN
fi

#echo "Running...."
set +e
timeout 2s ./sol <"$INP" > "$OUT"
status=$?
set -e

if [ $status -ne 0 ]; then
    exit $status
fi

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
rm -f "$OUT"

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

