#!/bin/sh
java -jar ../download/tester.jar -exec "python3 Jewels.py" -novis -seed $1
