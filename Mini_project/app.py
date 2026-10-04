
#dependencies
import os
import csv
from datetime import datetime

print("Welocme To Personal Expense Tracker: ")


#add Expenses
def add_expenses(description, amount):

    #Creating csv file to store the exp data
    with open("Personal_expense.csv",'a', newline="") as file:
        line = csv.writer(file)
        line.writerow([
            description, 
            amount, 
            datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            ])
    print("Expenses Recorded")


#view expenses
def View_expenses():
    total = 0

    if os.path.exists("Personal_expense.csv"):
        with open("Personal_expense.csv", "r") as file:
            read = csv.reader(file)
            for expense in read:
                print(f"\nItem name: {expense[0]}, Amount:{expense[1]}, Date: {expense[2]}")
                total += float(expense[1])
                print("Total Expenses : ", total)
    else:
        print("No Expenses Found!!!")

def main():
    while True:
        print("1. Add Expenses")
        print("2. view Expenses")
        print("3. Exit")

        choice = input("Please Select Any Option From Above :")

        if choice == "1":
            description= input("Please Enter Description: ")
            amount = float(input("Please Enter Amount: "))
            add_expenses(description, amount)

        elif choice == "2":
            View_expenses()

        elif choice == "3":
            print("Thank You !!!, You Have Exited Succesfully")
            break
        else:
            print("Invalid Choice! Please try again!")


if __name__ == "__main__":  # So that, if someone want to import a module, it will ignore the above main() function
    main()

