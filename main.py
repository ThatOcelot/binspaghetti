#Allows you to select whether you want to convert from binary to decimal or from decimal to binary
conv = input("Do you want to convert to binary or decimal? ")

if (conv == "decimal" or "Decimal"):
#Used for converting to decimal
	bin_num = input("Enter a binary number: ")
	try:
		dec_num = int(bin_num, 2)
		print("The decimal value is: " + str(dec_num))
		print("Done ✓")
	except ValueError:
		print("Invalid binary number")
elif (conv == "binary" or "Binary"):
#Used for converting to binary
	dec_num = int(input("Enter a decimal number: "))
	bin_num = bin(dec_num)
	print("The binary value is: " + str(bin_num))
	print("Done ✓")
else:
#Error message
        print("Error: Invalid Input")

