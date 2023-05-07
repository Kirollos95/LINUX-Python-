#Put Availabe Grocery In A Set 
Grocerry={'orange','apple','mango','Cucumber','ocra','peas'}
#Put Prices In A Dictionry
Prices = {
   'orange':15,
   'apple':30,
   'mango':32,
   'Cucumber':12,
   'ocra':8,
   'peas':10
}
Stock = {
   'orange':40,
   'apple':30,
   'mango':50,
   'Cucumber':20,
   'ocra':30,
   'peas':15
}
Admin = 'Admin@Grocery'
#Ask For User Type 
Mode = int(input('To Enter Administrator Mode Press 1\nFor Customers Press 2\n'))
while Mode == 1 :
 Password = input('Enter Password\n')
 if Password == Admin :
    Change = int(input('To Edit Grocery List Press 1 / To Edit Prices Press 2\n'))
    if Change == 1:
          Grocerry.add(input('Enter Items You Want To Add\n'))
          print('Grocerry List Edited Successfully')
    elif Change == 2:
          Item = input("Enter Item To Change It's Price\n")
          New_Price=int(input("Enter New Price\n"))
          Prices[Item]=New_Price
          print('Prices List Edited Successfully')
 elif Password != Admin : 
  print('Wrong Password')
  break
Mode = int(input('To Enter Administrator Mode Press 1\nFor Customers Press 2\n'))
while Mode == 2:
   Cost = 0
   print("Available Items In Kilos",Stock)
   print('Current Prices',Prices)
   #Please Specify Your Order 
   Order = input('Enter Item YOu Want To Order')
   #Please Specify Your Order's Quantity
   Quantity = int(input('Enter Quantity Of Item You Want'))
   Stock[Order]-=Quantity
   Cost = Cost + (Prices[Order]*Quantity)
   print('Your Order Costs ',Cost,' L.E')
   Ask= int(input('Do You Want Another Purchase ??\n Y:1 / N:2\n')) 
   if Ask == 2:
     Mode = 0 
print('Thank You For Your Visit ..')       