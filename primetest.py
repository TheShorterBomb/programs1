prime = int(input('Enter a number: '))
check = 0
for i in range(2, prime):
	if prime % i == 0:
		check += 1

if check != 0:
	
	for x in range(prime, 2*prime):
		check = 0
		for i in range(2, x-1):
			if x % i == 0:
				check += 1
		if check == 0:
			print(str(prime) + ' is not prime.')
			print('The closest prime after ' + str(prime) + ' is ' + str(x))
			break

else:
	print(str(prime) ++ ' is prime.')