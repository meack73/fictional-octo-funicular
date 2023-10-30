# encode - 




return result
# decode - NJ
def decoder(message):
	result = ""
	for number in message:
		new_number = str((int(digit) - 3) % 10)
		result += new_number
	return result

