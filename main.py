
def menu_display():
	print("Menu \n-------------")
	print("1. Encode \n2. Decode \n3. Quit")





# decode - NJ
def decoder(message):
	result = ""
	for number in message:
		new_number = str((int(digit) - 3) % 10)
		result += new_number
	return result


def encode_password(encode_input):
	encode_input_list = []
	for i in encode_input:
		i = int(i) + 3
		encode_input_list.append(i)
		encoded_string = "".join(map(str, encode_input_list))
	return encoded_string


def main():

	while True:
		menu_display()
		user_input = int(input("Please enter an option: "))
		if user_input == 1:
			encode_input = input("Please enter your password to encode: ")
			result = encode_password(encode_input)
			print("Your password has been encoded and stored!")
		if user_input == 2:
			password = decoder(result)
			print(f'The encoded password is {result}, and the original password is {password}.')
		if user_input == 3:
			break

if __name__ == "__main__":
	main()
