#!/bin/bash
#### Script to run pytiny compiler
### Author: Coolbrother
### Date: Sat, 19/12/2020
PYTHON="python3"
COMPILER="src/pytiny.py"
CC="gcc"

function comp {
    BN=$(basename -s .ty $1)
    TTOUTPUT=$(${PYTHON} ${COMPILER} $1 2>&1)
    if [ $? -ne 0 ]; then
        echo "${TTOUTPUT}"
    else
        mv out.c c/${BN}.c
        CCOUTPUT=$(${CC} -o build/${BN} c/${BN}.c)
        if [ $? -ne 0 ]; then
            echo "${CCOUTPUT}"
        else
            echo "${TTOUTPUT}"
        fi
    fi
}

if [ $# -eq 0 ]; then
    for i in $(ls examples/*.ty); do
        comp $i
    done
else
    comp $1
fi

exit 0
