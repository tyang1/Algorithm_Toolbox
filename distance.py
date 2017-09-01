import math

def medianString(dna,k):
	distance = math.pow(len(dna),k)
	print(int(math.pow(4,k)))
	for i in range(0, int(math.pow(4,k))-1):
		pattern = numtopattern(i,k)
		print(pattern)
		if distance > distancePS(pattern, dna):
			print (distancePS('GAC',dna))
			distance = distancePS(pattern, dna)
			median = pattern
	print (median)
	return median

def distancePS(pattern, dna):
	k = len(pattern)
	#print (k)
	distance = 0
	#t = dna.split()
	#print (t)
	for text in dna:
		hammingd = k*len(dna)
		for i in range(0,(len(text)-int(k)+1)):
			#print(text[i:(i+k)])
			if hammingd > hamming(pattern, text[i:(i+k)]):
				hammingd = hamming(pattern,text[i:(i+k)])
				#print(hammingd)
		distance = distance + hammingd
		#print(distance)
		#print(hammingd)
	print(distance)
	return distance

def hamming(text1, text2):
	count = 0
	for i in range(len(text1)):
		if text1[i] != text2[i]:
			count += 1
	#print (text1)
	return count

def numtopattern(index,k):
	if k == 1:
		return numbsym(index)
	prefixindex = index//4
	r = index%4
	symbol = numbsym(r)
	prefixpattern = numtopattern(prefixindex, k-1)
	return prefixpattern + symbol

def numbsym(index):
	num = {0:"A", 1:"C", 2:"G", 3:"T"}
	#print(num[index])
	return num[index]

import sys # you must import "sys" to read from STDIN
text= sys.stdin.read().split('\n')
k = text[0]
dna = text[1:-1]
#dna = sys.stdin.read()
with open("result.txt", 'a') as out:
	out.write(str(medianString(dna,int(k))))