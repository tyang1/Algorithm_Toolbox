def numtopattern(index,k):
	if k == 1:
		print (numbsym(index))
		return numbsym(index)
	prefixindex = index//4
	print(prefixindex)
	r = index%4
	print(r)
	symbol = numbsym(r)
	#print(symbol)
	prefixpattern = numtopattern(prefixindex, k-1)
	print(prefixpattern+symbol)
	return prefixpattern + symbol

def numbsym(index):
	num = {0:"A", 1:"C", 2:"G", 3:"T"}
	#print(num[index])
	return num[index]

import sys # you must import "sys" to read from STDIN
index, k = sys.stdin.read().splitlines()
print(index)
print(k)
with open("result.txt", 'a') as out:
	out.write(str(numtopattern(int(index),int(k))))