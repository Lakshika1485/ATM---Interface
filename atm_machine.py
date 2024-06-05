
import time

print("Please enter your card!!!")

time.sleep(4)

password = 1485

pin = int(input("Please insert your pin:"))

balance = 50000

if pin == password:

    while True:

        print("""
            1 == balance
            2 == withdrawl amount
            3 == deposit amount
            4 == exit
         """
              ) 
        
        try:
            option= int(input("Please enter your choice:"))

        except:
            
            print("Please enter valid option")



        if option == 1:
            
            print(f"Your current balance is {balance}")

        if option == 2:
           
            withdrawl_amount = int(input("Please enter the withdrawl amount: "))

            balance = balance - withdrawl_amount

            print(f"The amount debited by the account is {withdrawl_amount}")

            print(f"The updated balance in your account is {balance}")

        if option == 3:

            deposit_amount = int(input("Please enter the deposit amount"))

            balance = balance + deposit_amount

            print(f"The credited amount in your account is {deposit_amount}")

            print(f"The updated balance in your account is {balance}")

        if option == 4:
        
             break
        
else:
    
    print("Wrong pin entered. Please try again")