def raiseerror(cls,*args):
	raise cls(*args)

import re

def matchinglines(lines,regex):
	ret = []
	for i in range(len(lines)):
		match = re.match(regex,lines[i])
		if match is not None:
			ret.append(i)
	return ret

def walkback(lines,start,regex):
	possible_lines = matchinglines(lines,regex)
	possible_lines = [x for x in possible_lines if x<=start]
	possible_lines.sort()
	if len(possible_lines)>=1:
		return possible_lines[-1]

def walkup(lines,start,regex):
	possible_lines = matchinglines(lines,regex)
	possible_lines = [x for x in possible_lines if x>=start]
	possible_lines.sort()
	if len(possible_lines)>=1:
		return possible_lines[0]

if __name__=="__main__":
	with open("test.asm") as f:
		lines = [l.rstrip() for l in f]
	t1 = matchinglines(lines,"[^;]+(:{1,2})")
	print("Finding function declarations:")
	print(t1)
	print("Finding ignore line behind it:")
	t2 = walkback(lines,t1[0],"; ignore: (.*)$")
	print(t2)
	print("Testing to make sure ignore line isn't ahead of function declaration:")
	print(walkup(lines,t2,"[^;]+(:{1,2})")==t1[0])
