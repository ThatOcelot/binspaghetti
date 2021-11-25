Mes=input("Do you want to convert pounds or kilos: ")
if Mes == "kilos":
  C1= int("299792458")
  C2=(C1^2)
  M=int(input("how many kilos: "))
  E=(M*C2)
  print("the energy of the object is: "+str(E))
elif Mes =="pounds":
  C1= int("299792458")
  C2=(C1^2)
  pounds=int(input("How many pounds: "))
  Kilograms=(pounds*0.454)
  M=(Kilograms)
  E=(M*C2)
  print("the energy of the object is: "+str(E))
else:
  print("Error: Invalid_Input (only lowercase inputs:pounds or kilos(spelled like that))")
