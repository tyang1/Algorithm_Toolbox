def findOri (text):
	skew = [0]
	genome = text
	minimum  = []
	#print (skew[0])
	for i in (range(0, len(text)+1)):
		#print(skew[i])
		if genome[i] == ("A" or "T"):
			skew.append(skew[i])
		elif genome[i] == "G":
			skew.append(skew[i]+1)
			#skew += 1
		elif genome[i] == "C":
			skew.append(skew[i]-1)
			#skew -= 1
	print (skew)
	#print(skew)
	for i in (range(len(text)+1)):
		if skew[i] == min(skew):
				#print(min(skew))
			#if (skew[i+1] < skew[i+2] and skew[i+1] > skew[i]):
				minimum.append(str(i+1))
				#print(minimum)
	#print(min(skew))
	#print(skew)
	#print(len(skew))
	return str(minimum)

	

import sys # you must import "sys" to read from STDIN
text = sys.stdin.read()
#print(patternsearch(text,pattern))
with open("result.txt", 'a') as out:
	out.write(findOri(text))



