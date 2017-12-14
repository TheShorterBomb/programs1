x=0
for i in range(100000, 998001):
	if i // 100000 == i % 10:
		if (i // 10000 % 10) == (i % 100 // 10):
			if(i % 10000 // 1000) == (i % 1000 // 100):
				for a in range(100,999):
					for b in range(100,999):
						if a*b == i:
							print(i)