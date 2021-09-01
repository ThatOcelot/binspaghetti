sol = int(input("Enter your number: "))
num = int("1")
num2 = int("1")
num3 = (num * num2)
print("Computing....")
while sol >= num3:
    num3 = (num * num2)
    num2 = (num + num3)
    print(num3 - 1)
##very speedy
