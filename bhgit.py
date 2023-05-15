import random 
print("Welcome to EmployeeWage  ComputationProgram on Main branch")
randnumber=random.randint(0,1)
wagePerhour=20
fulldayhour=8
if(randnumber==0):
    print("employee is present")
    dailywage=wagePerhour*fulldayhour
    print(dailywage)
else:
    print("employee is absent")        