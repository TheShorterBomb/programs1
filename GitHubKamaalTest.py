# function to remove a character from a chosen position of a string
def remove_character(word, lint):
    x = ''
    # To add the letters before the removed character
    for i in range(lint):
        x = x + word[i]
    # Kamaal code here:

print(remove_character(input('Word?'), int(input('Letter to remove?'))))
