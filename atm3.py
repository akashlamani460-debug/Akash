Correct_Pin = "1234"
Balance = 10000
Enter_Pin = input("Enter your Pin")
if enter_Pin == correct_pin :
    print("Pin varified sucessfully")
    amount=int(input("Enter the withdraw amount"))
    if amount <= 0 :
        print("invaled amount")
    elif amount > Balance :
        print("insuffient fund")
     elif amount % 100 != 0:
        print("Enter multipals 100 Enter")
        Balance-= amount #Balance = Balance_amount
        print("sucessful transation")
        print("your remaind Balance Rs:", Balance)
else:
    print("Incorrect Pin")