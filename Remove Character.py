def remove_character(word, lint):
	x = ''
	for i in range(lint):
		x= x + word[i]
	for i in range(lint+1, len(word)):
		x= x + word[i]
	return x
print(remove_character(input('Word?'), int(input('Letter to remove?'))))
