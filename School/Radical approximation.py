n = int(input())
i = 1
t = 1/2
while i < n:
	t = 1/(2+t)
	i += 1
print(t+1)
