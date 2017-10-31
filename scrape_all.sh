#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0);pwd)
if [ $# -ne 2 ]; then
    echo "$0 indir outdir"
    exit 1
fi

for f in $(ls $1); do
    echo $f ${f%.html}.json
    python ${SCRIPT_DIR}/scrape.py $1/$f > $2/${f%.html}.json
done
