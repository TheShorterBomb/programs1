offset = int(input('Offset: '))
input = input('Write Text: ')
input = input.lower()
output = []
for character in input:
    number = ord(character) + offset
    output.append(number)
for character in output:
	print(chr(character))
