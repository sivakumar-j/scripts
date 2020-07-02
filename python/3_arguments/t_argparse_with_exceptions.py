#!/usr/bin/env python3.6
import argparse
import sys

#file used for testing is /home/cloud_user/scripts/python/file_manipulation/basics/new_friends.txt

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s verison 1.0')


args = parser.parse_args()


try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"File {args.filename} not found")
    sys.exit(1)
#except:
#    print("Hmm.. there seems to be unknown issue in the execution..!")
#    sys.exit(99)
else:
    with f:
        lines = f.readlines()
        lines.reverse()


    if limit:
        lines = lines[:limit] #diff from one in t_argparse_no_exceptions.py

    for line in lines:
        print(line)#.strip()[::-1]) logic to revese string
finally:
    print("All done..!")
