n = int(input('Which number in the sequence?'))
a = 0
b = 1
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    for x in range(n):
        if x % 2 == 0:
            a = a + b
        if x % 2 == 1:
            b = a + b
    if n % 2 == 0:
        print(a)
    else:
        print(b)
