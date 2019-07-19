#calculates the number of ways of reaching the top of n stairs, using 1,2, .. k steps at a time

from collections import defaultdict

def num_ways(n,k):
	numways = defaultdict( int )
	numways[0] = 1
	end = 0 #current position in the dict
	return num_ways2(numways,end,n,k)
def num_ways2(numways, end, n, k):
	if n <= end:
		return numways[n]
	while n > end:
		for m in range(end+1,end+k+1):
			numways[m] += numways[end]
		end += 1
	return numways[n]
	
if __name__ == "__main__":
	n = int(input("How many stairs are there? "))
	k = int(input("How many stairs can you climb at a time? "))
	print("There are {} ways to climb the stairs".format(num_ways(n,k)))