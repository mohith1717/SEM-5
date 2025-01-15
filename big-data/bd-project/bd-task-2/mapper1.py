#!/usr/bin/env python3

import sys

def process_input():
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        input=line.split(' ')
        if(len(input)>2):
            if(len(input)>3):
                 print(f"{input[2]} {input[0]} {input[1]} {input[3]} ")
            else:
                 print(f"{input[0]} {input[1]} {input[2]} {input[3]} {0}")
        else:
            print(f"{input[0]} {input[1]}")
if __name__ == "__main__":
    process_input()