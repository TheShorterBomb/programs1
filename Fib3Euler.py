
a=0
b=1
c=0
for x in range(100000):
	if x%2 == 0:
		a = a+b
		if a<4000000 and a%2==0:
			c = c+a	

	if x%2 == 1:
		b = a+b
		if b<4000000 and b%2==0:
			c = c+b		
	 
	

print(c)