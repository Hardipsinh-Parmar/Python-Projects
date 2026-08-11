amount = 5000
result = input("1 for checking balance     "
         "2 to deposit balance          "
         "3 to withdraw balance          "
         "4 for exit: ")
while result :
    if result == "1":
        print("Your balance is", amount)
        result = input("1 for checking balance     "
                       "2 to deposit balance          "
                       "3 to withdraw balance          "
                       "4 for exit: ")
    elif result == "2":
        deposit = float(input("Type deposit balance"))
        if 0>=deposit :
            print("Not possible")
        else:
         amount = amount + deposit
        print("Your balance is", amount)
        result = input("1 for checking balance     "
         "2 to deposit balance          "
         "3 to withdraw balance          "
         "4 for exit: ")
    elif result == "3":
        withdraw = float(input("Type withdraw balance"))
        if  withdraw < 0 or withdraw > amount or withdraw == 0  :
            print("Not possible")
        else:
         amount = amount - withdraw
        print("Your balance is", amount)
        result = input("1 for checking balance     "
                       "2 to deposit balance          "
                       "3 to withdraw balance          "
                       "4 for exit: ")
    elif result == "4":
        print("Thank you for using this program")
        break
    else:
        print("Please enter a valid option")
        result = input("1 for checking balance     "
                       "2 to deposit balance          "
                       "3 to withdraw balance          "
                       "4 for exit: ")
