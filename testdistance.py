def distancePS(pattern, dna):
	k = len(pattern)
	#print (k)
	distance = 0
	t = dna.split()
	#print (t)
	for text in t:
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

import sys # you must import "sys" to read from STDIN
pattern,dna= sys.stdin.read().splitlines()
#lenn = len(pattern)
#print(pattern)
#print(dna)
with open("result.txt", 'a') as out:
	out.write(str(distancePS(pattern,dna)))