lowerAlphabet = 'abcdefghijklmnopqrstuvwxyz'
upperAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 3
newMessage = ''

message = input('Please enter a message: ')
key = int(input('Please enter a key: '))

for character in message:
	if character in lowerAlphabet:
		position = lowerAlphabet.find(character)
		newPosition = (position + key) % 26
		newCharacter = lowerAlphabet[newPosition]
		newMessage += newCharacter			
	elif character in upperAlphabet:
		position = upperAlphabet.find(character)
		newPosition = (position + key) % 26
		newCharacter = upperAlphabet[newPosition]
		newMessage += newCharacter	
	else:
		newMessage += character
	
print('The new message is: ', newMessage)