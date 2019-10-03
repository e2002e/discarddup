#!/usr/bin/python2.7
import sys

file1 = open(sys.argv[1], 'r')
file2 = open(sys.argv[2], 'rw+')
tmp = file1.readlines()
tmp2 = file2.readlines()

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
