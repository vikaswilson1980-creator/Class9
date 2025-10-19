attendence=int(input("Enter attendence percentage:"))

medical=input("Do you have any medical  certificate y or n:")

if(medical=="y"):
    print("You are eligible")
else:
    if(attendence>=75):
     print("You are elegible")
    else:
       print("You are not allowed")