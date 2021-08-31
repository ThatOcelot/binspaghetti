conv1 = input("Do you want to convert from binary, hexadecimal, or decimal? ")

if (conv1 == "binary"):
	bin_num = input("Enter a binary number: ")
	dec_num = int(bin_num, 2)
	conv2 = input("Do you want to convert to hexadecimal or decimal? ")
	if (conv2 == "hexadecimal"):
		hex_num = hex(dec_num)
		print(hex_num)
	elif (conv2 == "decimal"):
		print(dec_num)
	else:
		print("Error: Invalid Input")
elif (conv1 == "decimal"):
	dec_num = int(input("Enter a decimal number: "))
	conv2 = input("Do you want to convert to hexadecimal or binary? ")
	if (conv2 == "hexadecimal"):
		hex_num = hex(dec_num)
		print(hex_num)
	elif (conv2 == "binary"):
		bin_num = bin(dec_num)
		print(bin_num)
	else:
		print("Error: Invalid Input")
elif (conv1 == "hexadecimal"):
	hex_num = input("Enter a hexadecimal number: ")
	dec_num = int(hex_num, 16)
	conv2 = input("Do you want to convert to decimal or binary? ")
	if (conv2 == "decimal"):
		print(dec_num)
	elif (conv2 == "binary"):
		bin_num = bin(dec_num)
		print(bin_num)
	else:
		print("Error: Invalid Input")
else:
	print("Error: Invalid Input")
