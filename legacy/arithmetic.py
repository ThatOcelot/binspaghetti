operation = input("What operation do you want to use? ")

if operation == "division":
  num1 = float(input("Enter a number to be your dividend: "))
  num2 = float(input("Enter a number to be your divisor: "))
  quotient = (num1 / num2)
  remainder = (num1 % num2)
  print("Your quotient is " + str(int(quotient)))
  print("Your remainder is " + str(int(remainder)))
elif operation == "addition":
  num1 = float(input("Enter your first addend: "))
  num2 = float(input("Enter your second addend: "))
  nsum = (num1 + num2)
  print("Your sum is " + str(nsum))
elif operation == "subtraction":
  num1 = float(input("Enter your minuend: "))
  num2 = float(input("Enter your subtrahend: "))
  difference = (num1 - num2)
  print("Your difference is " + str(difference))
elif operation == "multiplication":
  num1 = float(input("Enter your multiplier: "))
  num2 = float(input("Enter your multiplicand: "))
  product = (num1 * num2)
  print("Your product is " + str(product))
elif operation == "exponentation":
	num1 = float(input("Enter your base: "))
	num2 = float(input("Enter your exponent: "))
	power = (num1 ** num2)
	print("Your result is " + str(power))
else:
  print("Not a valid operation")
