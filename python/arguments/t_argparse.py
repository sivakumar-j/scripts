#!/usr/bin/env python3.6
import argparse

#file used for testing is /home/cloud_user/scripts/python/file_manipulation/basics/new_friends.txt

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

with open(args.filename) as f:
    v_lines = f.readlines()
    print(v_lines)
    v_lines.reverse()
    print(v_lines)

if args.limit: #if the --limit is provided this will be executed,Else all lines will be considered
    v_lines = v_lines[:args.limit]

for line in v_lines:
    print(line)#.strip()[::-1]) logic to revese string
