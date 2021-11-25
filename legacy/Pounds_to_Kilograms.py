PKG=input("what would you like to convert \nPounds\nOr\nKilograms")

if(PKG == "Pounds")
  PV=int(input("Pounds: "))
  try:

  print(PV*0.454)
 except ValueError:
         print("Enter a real value")
elif (PKG == "Kilograms")
      KGV=int(input("Kilograms: "))
      try:
      
      print(KGV*2.205)
else:
    print("Error: Invalid_unit")
      

    
