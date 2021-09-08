operation = input("What operation do you want to use? ")

if operation == "division":
  num1 = float(input("Enter a number to be your dividend: "))
  num2 = float(input("Enter a number to be your divisor: "))
  quotient = (num1 / num2)
  remainder = (num1 % num2)
  print(int(quotient))
  print(int(remainder))
elif operation == "addition":
  num1 = float(input("Enter  your first number: "))
  num2 = float(input("Enter your second number: "))
  nsum = (num1 + num2)
  print(int(nsum))
elif operation == "substraction":
  num1 = float(input("Enter  your first number: "))
  num2 = float(input("Enter your second number: "))
  difference = (num1 - num2)
  print(int(difference))
elif operation == "multiplication":
  num1 = float(input("Enter  your first number: "))
  num2 = float(input("Enter your second number: "))
  product = (num1 * num2)
  print(int(product))
else:
  print("Not a valid operation")
