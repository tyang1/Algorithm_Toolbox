def motifenum(dna,k,d):
	patt = set()
	new = set()
	search = set()
	s = []
	entry = dna.splitlines()
	print(entry)
	for e in entry:
		for i in range(0, (len(e)-int(k)+1)):
			kmer = e[i:(i+k)]
			s.append(kmer)
			print(kmer)
			patternd = neighbors(kmer,d)
			search.update(patternd)
	print(search)
	for each in search:
		count = 0
		for e in entry:
			for i in range(0, (len(e)-int(k)+1)):
				#print(each)
				#print(dna[i:(i+k)])
				if hamming(each, e[i:(i+k)]) <= d:
					count += 1
					break
				else:
					continue
			if count == len(entry):
				patt.add(each)
			else:
				continue

	print (patt)
	#return pattern
	return " ".join(map(str,patt))

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
			#print (text)
			#print(suffix(pattern))
			for each in nucleotide:
				neighborhood.add(each + text)
				#print(neighborhood)
		else:
			neighborhood.add(firstsymb(pattern) + text)
			#print (neighborhood)
	#print (neighborhood)
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
	#print (text1)
	return count

import sys # you must import "sys" to read from STDIN
number = sys.stdin.readline().split()
k = int(number[0])
d = int(number[1])
print(k)
print(d)
text = sys.stdin.read()
print(text)
with open("result.txt", 'a') as out:
	out.write(str(motifenum(text, k, d)))
