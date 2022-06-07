# Program for Income_Tax
total_income = int(input("Enter total income "))
H_R_A = int(input("Enter HRA "))*12
od = int(input("Enter other deductions "))
if(od > 80000):
    od = 80000
Income_tax = total_income-(H_R_A+od)
if(Income_tax < 300000):
    print("You are tax free")
elif(Income_tax < 600000 and Income_tax > 300000):
    print("The tax amount is", Income_tax*0.1)
elif(Income_tax < 1000000 and Income_tax > 600000):
    print("The tax amount is", Income_tax*0.15)
else:
    print("The tax amount is", Income_tax*0.2)
