#RAM

while True :
    try :
        User_Choice = int(input("Enter 1 to add expense , 2 to check all expenses or 3 to check for particular categories : "))
        break
    except Exception  :
        print("Please enter a valid number.")

if User_Choice == 1 :
    while True :
        categories = [ x.strip() for x in input("Please enter all the categories seperated by commas :)  ").split(",")]
        expenses = list(map(float,input("Please enter the respective expenses seperated by commas :)  ").split(",")))
        Notes = [ x.strip() for x in input("Enter the corresponding notes seperated by commas :)  ").split(",")]

        if len(categories) == len(expenses) == len(Notes) :
            records = list(zip(categories, expenses, Notes))
            with open("expenses.txt", "a") as file:
                for category, amount, note in records:
                    file.write(f"{category},{amount},{note}\n")
            print("Expenses saved successfully!")
            break
        else : 
            print("Number of categories, expenses and notes must be same") 

elif User_Choice == 2 :

    print("-" * 45)
    print(f"{'Category':<15} {'Expense':>10} {'Notes':>10}")
    print("-" * 45)
    total = 0

    with open("expenses.txt", "r") as file:
        for line in file:
            category, amount, note = line.strip().split(",")
            amount = float(amount)

            print(f"{category:<15} {amount:>10} {note:>10}")
            total += amount
    print("-" * 45)
    print(f"{'Total':<15} {total:>10}")
    print("-" * 45)

elif User_Choice == 3 :
    search = [ x.strip() for x in input("Enter categories separated by commas: ").split(",")]
    subtotal = 0
    print("-" * 45)
    print(f"{'Category':<15} {'Expense':>10} {'Notes':>10}")
    print("-" * 45)

    with open("expenses.txt", "r") as file:
        for line in file:
            category, amount, note = line.strip().split(",")
            if category in search:
                amount = float(amount)
                print(f"{category:<15} {amount:>10} {note:>10}")
                subtotal += amount
    print("-" * 45)
    print(f"{'Subtotal':<15} {subtotal:>10}")

else :
    print("Please enter the choice from 1/2/3 :)")































