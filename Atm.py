Balance=100


print('''Press 1 for Deposit
      Press 2 for WIthrawl
      Press 3 for Show Balance''')
a=eval(input())
if a==1:
    print('Enter Amount')
    amount=eval(input())
    print(Balance+amount)
    print(amount)
elif a==2:

    print("Enter Amount To Withrawl")
    w=eval(input())
    print(Balance-w)
    
if w>100:
    print("Insufficient Balance")

if w<100:
    print("Enter amount To Withrawl")
    print(Balance-w)
    print(Balance)
    if a==3:
        print(Balance)

    
