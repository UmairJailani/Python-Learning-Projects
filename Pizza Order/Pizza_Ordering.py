print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
extra_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
s = 15
m = 20
l = 25
pepperoni = 5
cheese = 5
bill = 0

if size == "S":
    bill += s
    if extra_pepperoni == "Y" and extra_cheese == "N":
        bill += pepperoni
        print("Your bill for a Small pepperoni Pizza is $" + str(bill))
    elif extra_pepperoni == "N" and extra_cheese == "Y":
        bill += cheese
        print("Your bill for a Small cheese Pizza is $" + str(bill))
    elif extra_pepperoni == "Y" and extra_cheese == "Y":
        bill += pepperoni
        bill += cheese
        print("Your bill for a small pizza with Pepperoni & Cheese is $" + str(bill))
    elif extra_pepperoni == "N" and extra_cheese == "N":
        print("Your bill for a small pizza is $" + str(bill))
    else:
        print("Please enter S, M, or L! Pepperoni or Cheese! Please try again!")
elif size == "M":
    bill += m
    if extra_pepperoni == "Y" and extra_cheese == "N":
        bill += pepperoni
        print("Your bill for a medium pepperoni Pizza is $" + str(bill))
    elif extra_pepperoni == "N" and extra_cheese == "Y":
        bill += cheese
        print("Your bill for a Medium cheese Pizza is $" + str(bill))
    elif extra_pepperoni == "Y" and extra_cheese == "Y":
        bill += pepperoni
        bill += cheese
        print("Your bill for a Medium pizza with Pepperoni & Cheese is $" + str(bill))
    elif extra_pepperoni == "N" and extra_cheese == "N":
        print("Your bill for a Medium pizza is $" + str(bill))
    else:
        print("Please enter S, M, or L! Pepperoni or Cheese! Please try again!")
elif size == "L":
    bill += l
    if extra_pepperoni == "Y" and extra_cheese == "N":
        bill += pepperoni
        print("Your bill for a Large pepperoni Pizza is $" + str(bill))
    elif extra_pepperoni == "N" and extra_cheese == "Y":
        bill += cheese
        print("Your bill for a Large cheese Pizza is $" + str(bill))
    elif extra_pepperoni == "Y" and extra_cheese == "Y":
        bill += pepperoni
        bill += cheese
        print("Your bill for a Large pizza with Pepperoni & Cheese is $" + str(bill))
    elif extra_pepperoni == "N" and extra_cheese == "N":
        print("Your bill for a Large pizza is $" + str(bill))
    else:
        print("Please enter S, M, or L! Pepperoni or Cheese! Please try again!")
else:
    print("Please enter S, M, or L")
