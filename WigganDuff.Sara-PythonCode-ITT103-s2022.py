#Author: Sara Wiggan-Duff
#Date Created: April 29, 2022
#Course: ITT103
#Purpose: To create a program for JamEx Ltd to calculate and print commission rate for sales persons

 
import sys
import time


#This is class1 function
def class1():
    sales_amount = int(input("Enter sales amount:"))
    if sales_amount <= 1000:
        rate = sales_amount * 0.06
        print("Commission rate is:", rate)
    elif sales_amount > 1000 and sales_amount < 2000:
        rate = sales_amount * 0.07
        print("Commission rate is:", rate)
    elif sales_amount > 2000:
        rate = sales_amount*0.1
        print("Commission rate is:", rate)
    else:
        print("You have entered an invalid option")
        menu()

#This is class2 function
def class2():
    sales_amount = int(input("Enter sales amount: "))
    if sales_amount < 1000:
      rate = sales_amount*0.04
      print("Commission rate is:", rate)
    elif sales_amount >1000:
      rate = sales_amount*0.06
      print("Commission rate is 6:", rate)
    else:
      print("You have entered an invalid option")
      menu()

#this is class3 function
def class3():
   sales_amount = int(input("Enter sales amount: "))
   rate = sales_amount*0.045
   print("Commission rate is:", rate)
   menu()

#This is the quit or exit function
def quit():
   print ("The system will now exit....")
   time.sleep(1)
   sys.exit()

#This is the Main Menu function
def menu():
  print("******Welcome to JamEx Limited Rate Calculator*******")
  print("*************Main Menu************")
  time. sleep(1)

  #prompt user to enter sales person number
  option = input("Enter sales person number: ")
  #prompt user to select class 
  option = input( """
                        A: class1
                        B: class2
                        C: class3
                        Q: Quit

                        Please Enter a class option A, B, C or Q to quit:
  
  
  """)
  #read class and call function for each class
  if option == "A" or option =="a":
    class1()
  elif option == "B" or option =="b":
    class2()
  elif option == "C" or option =="c":
    class3()
  elif option == "Q" or option =="q":
    quit()
  else:
    print("Please enter a valid option")
    menu()

menu()

