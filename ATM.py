import time
#Start Of Project 
print('welcome to the Bank')
#A Tuple That Carries Virtual Passwords Database
Passwords=('1023','1233','6523')
#A Dictionry To Link Password To Each User
Accounts = {
     'Ahmed':Passwords[0],
     'Peter':Passwords[1],
     'John':Passwords[2]
}
#A Dictionry Having The Accounts Balances
Balance={'Ahmed':12000,'Peter':4000,'John':3000000}
#Asking For Password
Password=input('Please Enter Your Password\n')
#Password Check
if Password == Accounts['Ahmed'] :
    print('Please Wait ..')
    time.sleep(1)
    print('Welcome Ahmed')
    while True :
        #Please Choose Your Operation
        Operation=input('To Withdraw Please Press : 1 \nTo Deposit Please Press : 2\nTo Check Your Balance Please Press : 3\n')
        #Withdrawal
        if Operation == '1' :
        #Ask For Withdrawing Amount
           Amount=input('Please Enter The Amount ..\n')
                 #Find If There's Enough Balance
           if int (Amount) <= Balance['Ahmed']:
                 Balance['Ahmed'] -= int (Amount)
                 print('Please Recieve Your Money \n Your Current Balance = ',Balance['Ahmed'] , 'L.E') 
           elif int (Amount) > Balance['Ahmed']:
                 print('Not Enough Balance')
                 End=input('For Another Operation Press Y \n For Ending Process Press N\n')
                 if End == 'N':
                  print('Thank You For Using The Bank ..')
                 break          
        elif Operation == '2' :
                Incoming = input('Please Enter The Amount You Wish To Deposit & Deposit Your Money ..\n')
                 #Calculate The New Balance
                Balance['Ahmed']+=int(Incoming)
                print('You Entered ',int(Incoming),' L.E\nYour New Balance = ',Balance['Ahmed'], 'L.E' )
                End=input('For Another Operation Press Y \n For Ending Process Press N\n')
                if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break   
        elif Operation == '3' :
                print("Your Balance is = ",Balance['Ahmed']," L.E")
                End=input('For Another Operation Press Y \n For Ending Process Press N\n')
                if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break                       
        else :
            print('Invalid Operation')
            End=input('For Another Operation Press Y \n For Ending Process Press N\n')
            if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break       
elif  Password == Accounts['Peter']:
    print('Please Wait ..')
    time.sleep(1)
    print('Welcome Peter')
    while True :
        #Please Choose Your Operation
        Operation=input('To Withdraw Please Press : 1 \nTo Deposit Please Press : 2\nTo Check Your Balance Please Press : 3\n')
        #Withdrawal
        if Operation == '1' :
        #Ask For Withdrawing Amount
           Amount=input('Please Enter The Amount ..\n')
                 #Find If There's Enough Balance
           if int (Amount) <= Balance['Peter']:
                 Balance['Peter'] -= int (Amount)
                 print('Please Recieve Your Money \n Your Current Balance = ', Balance['Peter'], 'L.E') 
           elif int (Amount) > Balance['Ahmed']:
                 print('Not Enough Balance')
                 End=input('For Another Operation Press Y \n For Ending Process Press N\n')
           if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break          
        elif Operation == '2' :
                Incoming = input('Please Enter The Amount You Wish To Deposit & Deposit Your Money ..\n')
                 #Calculate The New Balance
                Balance['Peter']+=int(Incoming)
                print('You Entered ',int(Incoming),'L.E\nYour New Balance = ',Balance['Peter'], 'L.E' )
                End=input('For Another Operation Press Y \n For Ending Process Press N\n')
                if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break      
        elif Operation == '3' :
                print("Your Balance is = ",Balance['Peter']," L.E")
                End=input('For Another Operation Press Y \n For Ending Process Press N\n')
                if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break                              
        else :
            print('Invalid Operation')
            End=input('For Another Operation Press Y \n For Ending Process Press N\n')
            if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break          
elif Password == Accounts['John']:
    print('Please Wait ..')
    time.sleep(1)
    print('Welcome John')
    while True :
        #Please Choose Your Operation
        Operation=input('To Withdraw Please Press : 1 \nTo Deposit Please Press : 2\nTo Check Your Balance Please Press : 3\n')
        #Withdrawal
        if Operation == '1' :
        #Ask For Withdrawing Amount
           Amount=input('Please Enter The Amount ..\n')
                 #Find If There's Enough Balance
           if int (Amount) <= Balance['John']:
                 Balance['John'] -= int (Amount)
                 print('Please Recieve Your Money \n Your Current Balance = ', Balance['John'], 'L.E') 
           elif int (Amount) > Balance['Ahmed']:
                 print('Not Enough Balance')
                 End=input('For Another Operation Press Y \n For Ending Process Press N\n')
           if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break          
        elif Operation == '2' :
                Incoming = input('Please Enter The Amount You Wish To Deposit & Deposit Your Money ..\n')
                 #Calculate The New Balance
                Balance['John']+=int(Incoming)
                print('You Entered ',int(Incoming),'L.E\nYour New Balance = ',Balance['John'] ,'L.E' )
                End=input('For Another Operation Press Y \n For Ending Process Press N\n')
                if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break 
        elif Operation == '3' :
                print("Your Balance is = ",Balance['John']," L.E")
                End=input('For Another Operation Press Y \n For Ending Process Press N\n')
                if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break                                   
        else :
            print('Invalid Operation')
            End = input('For Another Operation Press Y \n For Ending Process Press N\n')
            if End == 'N':
                 print('Thank You For Using The Bank ..')
                 break          
else :
    print('Please Wait ..')
    time.sleep(1)
    print('Wrong Password .. Recieve Your Card Please')

