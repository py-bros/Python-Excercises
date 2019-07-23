#GET INPUT
length = int(input())
array = [int(x) for x in input().split(' ')]

#FUCNTION TO CHECK IF INCREASING
def check(array):
	l = len(array)
	for i in range(1, l):
		if (array[i-1]) > (array[i]):
			return False
	return True

parts = 1

while True:
	
	for i in range(parts):
		temp = array[i*length//parts:(i+1)*length//parts]
		#print (temp)
		if check(temp) == True:
			print (length//parts)
			exit()
		
	parts *= 2
	
	if length//parts == 1:
		print (1)
		exit()
