import math
a =int(raw_input())
b = int(raw_input())
c = int(raw_input())
m = max(a,b,c)
print ('the maximum value of the 3 is %d and square root of the max. is %f') % (m,math.sqrt(m))

def max(x,y,z):
	max = x

	if y > max:
		max = y

	if z > max:
		max = z
	return max 


