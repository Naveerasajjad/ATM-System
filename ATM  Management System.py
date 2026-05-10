balance=int(input("Enter amount of balace:"))
while True:
    print("""
    1.Check balance
    2.Withdraw
    3.Exit
    """)
    choice=input("Enter Choice:")
    if choice=="1":
        print("Your balance is",balance)
    elif choice=="2":
        try:
            amount=int(input("Enter amount:"))
            if amount<=balance:
                balance-=amount
                print("Withdraw Successful")
            else:
                print("Insufficient Balance")
        except:
                print("invalid input")
    elif choice=="3":
        print("Thank You") 
        break
    else:
        print("invalid choice")       