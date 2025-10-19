unit=int(input("Enter the number of unites you have consumed:"))
if(unit<50):
    amount=unit*2.60
    surcharge=25
elif(unit<=100):
    amount=130+((unit-50)*3.25)
    surcharge=35
elif(unit<=200):
    amount=130+162.50+((unit-100)*5.26)
    surcharge=45
else:
    amount=130+162.50+526((unit-100)*8.25)
    surcharge=75
total=amount+surcharge
print("You electricity bill is = %.2f"%total)

    