expenses=[]

while True : 
    
    try :
        a=int(input("Press 1 to add a new Expense \npress 2 to see the total expenses\npress 3 to see each expense\npress 4 to exit\n"))
    except : 
        print("wrong answer , Please make sure you press 1 or 2 or 3 or 4\n")
        continue 
    if a == 1 : 
        while True :
            try : 
                expenses.append(float(input("Please enter your new expense in numbers (e.g 100 , 50) \n")))
                try :
                    b=int(input("Do you want to add another expense? {press 1 for yes and 2 for no }\n"))
                    if b ==  1 :
                        continue 
                    elif b == 2 :
                        break
                    else :
                        print("your options are only 1 (yes) or 2 (no) so try again\n")
                        continue
                except :
                    print ("your answer must be a number , try again")
                    continue 

            except :
                print("Please re-enter your expense in numbers only\n")
                continue
    elif a == 2 :
        total=0
        for exp in expenses :
            total+=exp 
        print(f"your total expenses = {total}")
    elif a == 3  : 
        print("your expenses are\n")
        for exp in range (len(expenses)) : 
            print(f"{exp+1} = {expenses[exp]}\n")
    elif a == 4 : 
        break
                