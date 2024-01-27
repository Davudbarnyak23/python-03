print("\n------------------------------")
print("          учні в класі")
print("------------------------------",end="\n")

girls = int(input("дівчат: "))
boys = int(input("хлопців: "))

print(type(girls), type(boys), end="\n\n")

ugni = girls + boys
progentg = girls * 100 // ugni
progentb = 100 - progentg 

print ("дівчат" + str(progentg) + "%, хлопців" + str(progentb) + "%")


print("\n\n\n")