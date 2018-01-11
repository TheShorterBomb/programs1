n = int(input('Is this number in the fibonacci sequence?'))
a=0
b=1
if n == 1:
	print('Yes', n, 'is in the fibonacci sequence.')
elif n == 2:
	print('Yes', n, 'is in the fibonacci sequence.')
else:
	for x in range(n):
		if x%2 == 0:
			a = a+b
		if x%2 == 1:
			b = a+b
		if n == a or n == b:
			print('Yes', n, 'is in the fibonacci sequence.')
			break
	if n != a and n != b:
		print('No', n, 'is not in the fibonacci sequence.')