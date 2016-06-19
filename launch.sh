#!/bin/bash

python mywebserver.py &
PID1="$!"
python pywb.py $PID1
