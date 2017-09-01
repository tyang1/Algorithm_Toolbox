def neighbors(pattern,d):
	if d == 0:
		return set(pattern)
	if len(pattern) == 1:
		return {"A", "C","G", "T"}
	neighborhood = set()
	suffixneighbors = neighbors(suffix(pattern), d)
	#print (suffix(pattern))
	nucleotide = {"A", "C", "T", "G"}
	for text in suffixneighbors:
		if hamming(suffix(pattern), text) < d:
			#print (suffix(pattern))
			for each in nucleotide:
				neighborhood.add(each + text)
		else:
			neighborhood.add(firstsymb(pattern) + text)
	print (neighborhood)
	return neighborhood
	#return "\n".join(item[0] for item in list(neighborhood))
	#return " ".join(map(str,neighborhood))

def firstsymb(pattern):
	return pattern[0]

def suffix(pattern):
	return pattern[1:]

def hamming(text1, text2):
	count = 0
	for i in range(len(text1)):
		if text1[i] != text2[i]:
			count += 1
	#print (count)
	return count

import sys # you must import "sys" to read from STDIN
pattern, d= sys.stdin.read().splitlines()
with open("result.txt", 'a') as out:
	out.write(neighbors(pattern,int(d)))
