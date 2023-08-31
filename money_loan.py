#get deteails of loan 

money_owed = float(input("how much money do you owe? \n"))
apr = float(input("what's the annual percentage rate of the loan? \n"))
payment = float(input("how much will you pay off each month? \n"))
months = int(input("how many months do you want to see the results for? \n"))

monthly_rate= apr/100/12

for i in range(months):
    #calculate interest to pay
    interest_paid = money_owed * monthly_rate
    
    #add interest
    money_owed= money_owed + interest_paid
    
    if (money_owed - payment < 0):
        print("the last payment is", money_owed)
        print("you paid off the loan in", i+1, "months")
        break #we dont want any more code in this lop
    
    #make payment 
    money_owed = money_owed - payment
    
    print("paid", payment, "of which ", interest_paid, "was interest ", end=' ')
    print("now i owe", money_owed)