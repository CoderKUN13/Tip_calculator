#Display Introduction Message.
print('Welcome to Tip Calculator')

#Establishing various inputs that are required.
amount = int(input("Enter the total bill amount: "))
tip = int(input("Enter the amount of tip 5%, 10%, 12%: "))
ppl = int(input("Enter the number of people to split the bill with: "))


#Implementation of the logic
tip_amt = amount * tip / 100
formula = (amount + tip_amt) / ppl

#Using round() function upto 2 decimals
final_split = round(formula, 2)

#Printing the final output using f-String
print(f"Each Person has to pay {final_split} rupees.")


