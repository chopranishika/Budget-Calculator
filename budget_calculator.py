userBudget=float(input("please enter your total monthly budget for this month:"))
moreExpenses='y'
totalExpenses=0
while (moreExpenses == 'y'):
    userExpense=float(input("enter an expense:"))
    totalExpenses=totalExpenses+userExpense
    moreExpenses= input("do u have more expenses:? type y for yes n for no")
print()

if totalExpenses>userBudget:
    print("you were over your budget of"+userBudget+"rupees","by"+totalExpenses-userBudget,"rupees")

elif userBudget>totalExpenses:
    print("you were under your budget of" , userBudget ,"rupees", "by" , userBudget-totalExpenses,"rupees")

else:
    print("you used your budget of"+userBudget,"rupees",".")