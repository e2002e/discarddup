#!/usr/bin/python2.7
import sys
import argparse

parser = argparse.ArgumentParser(description="remove duplicate lines from files")
parser.add_argument("FILE1", type=argparse.FileType('r'), metavar="file1", help="file to test with")
parser.add_argument("FILE2", type=argparse.FileType('rw+'), metavar="file2", help="file to operate on")
parser.parse_args()
tmp = parser.file1.readlines()
tmp2 = parser.file2.readlines()

a = 0

for line1 in iter(tmp):
	x = 0
	for line2 in iter(tmp2):
		if line1 == line2:
			del(tmp2[x])
			a += 1
		x += 1
print "removed %d duplicates" % a

file1.close()	
file2.seek(0)
file2.truncate()
file2.writelines(tmp2)
file2.close()
