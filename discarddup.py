#!/usr/bin/python2.7
import sys
import argparse

parser = argparse.ArgumentParser(description="remove duplicate lines from files")
parser.add_argument("FILE1", type=argparse.FileType('r'), help="file to test with")
parser.add_argument("FILE2", type=argparse.FileType('rw+'), help="file to operate on")
args = parser.parse_args()
tmp = args.FILE1.readlines()
tmp2 = args.FILE2.readlines()

a = 0

for line1 in iter(tmp):
	x = 0
	for line2 in iter(tmp2):
		if line1 == line2:
			del(tmp2[x])
			a += 1
		x += 1
print "removed %d duplicates" % a

args.FILE1.close()	
args.FILE2.seek(0)
args.FILE2.truncate()
args.FILE2.writelines(tmp2)
args.FILE2.close()
