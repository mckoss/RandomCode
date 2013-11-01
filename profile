#!/bin/bash

if [ "$#" != "1" ]; then
    echo "Usage: profile N"
    echo "    Run the python profiler on eulerN.py."
    exit 1
fi

FILE=euler${1}.py

echo Profiling $FILE...
python -m cProfile -s cumulative $FILE
