#!/usr/bin/env python
from utils import *
import re

split_re = re.compile("[\s]")


def read_file(input_fh):
    with input_fh:
        return [tuple(split_re.split(line.strip())) for line in input_fh]

def sort_lines(lines):
    return sorted(lines, key=lambda x: len(x[1]))

if len(sys.argv) != 2:
    die("Program requires exactly 1 argument")

input_file_name = sys.argv[1]

try:
    input_fh = open(input_file_name, "rb")
    lines = read_file(input_fh)
    sorted_lines = sort_lines(lines)
    print lines
except IOError:
    die("Could not read file: %s" % input_file_name)
