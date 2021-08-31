#Asks what number system you want to convert from.
conv1 = input("Do you want to convert from binary, hexadecimal, or decimal? ")

#Conversions from binary
if (conv1 == "binary"):
	bin_num = input("Enter a binary number: ")
	dec_num = int(bin_num, 2)
	conv2 = input("Do you want to convert to hexadecimal or decimal? ")
	#Conversions from binary to hex
	if (conv2 == "hexadecimal"):
		hex_num = hex(dec_num)
		print(hex_num)
	#Conversions from binary to decimal
	elif (conv2 == "decimal"):
		print(dec_num)
	else:
		print("Error: Invalid Input")
#Conversions from decimal
elif (conv1 == "decimal"):
	dec_num = int(input("Enter a decimal number: "))
	conv2 = input("Do you want to convert to hexadecimal or binary? ")
	#Conversions from decimal to hex
	if (conv2 == "hexadecimal"):
		hex_num = hex(dec_num)
		print(hex_num)
	#Conversions from decimal to binary
	elif (conv2 == "binary"):
		bin_num = bin(dec_num)
		print(bin_num)
	else:
		print("Error: Invalid Input")
#Conversions from hexadecimal
elif (conv1 == "hexadecimal"):
	hex_num = input("Enter a hexadecimal number: ")
	dec_num = int(hex_num, 16)
	conv2 = input("Do you want to convert to decimal or binary? ")
	#Conversions from hex to decimal
	if (conv2 == "decimal"):
		print(dec_num)
	#Conversions from hex to binary
	elif (conv2 == "binary"):
		bin_num = bin(dec_num)
		print(bin_num)
	else:
		print("Error: Invalid Input")
else:
	print("Error: Invalid Input")
