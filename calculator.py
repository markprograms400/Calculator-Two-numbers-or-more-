print("""
Welcome to my calculator!
Would you like to calculate (two numbers? or more?)
""")

def twonumbers():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  return num1, num2

def addition(x, y):
  result = x + y
  print(result)

def subtraction(x, y):
  result = x - y
  print(result)
  
def multiplication(x, y):
  result = x * y
  print(result)
def division(x, y):
  result = x / y
  print(result)

def options():
   print("""
What would you like to calculate? 
1. Addition
2. Substraction
3. Multiplication
4. Division
         """)

#--------------------------------------MORE FUNCTIONS--------------------------------------------------
def more(): 
   numberlist = []
   print("Enter your number here")
   while True: 
      numberinput = input("Enter your numbers (Press Enter to stop): ")
      if numberinput == "":
         break
      numberlist.append(int(numberinput))
   return numberlist

def addition_more(numbers):
   result = sum(numbers)
   print(f"Your total is {result}")

def subtraction_more(numbers): 
   result = numbers[0]
   for n in numbers[1:]:
      result -= n 
   print(f"Your total is {result}")

def multiplication_more(numbers):
   result = numbers[0]
   for n in numbers[1:]:
      result *= n
   print(f"Your total is {result}")

def division_more(numbers):
   result = numbers[0]
   for n in numbers[1:]: 
      result /= n 
   print(f"Your total is {result}")
   
userchoice = input("Please enter your choice (two numbers), or (more): ")
   

#--------------------------------------------------TWO NUMBERS------------------------------------------------------   
if userchoice == "two numbers": 
   num1, num2 = twonumbers()
   options()
   option = int(input("Enter a number between (1-4), or 0 to exit: "))

   if option == 1: 
      addition(num1, num2)
   elif option == 2:
      subtraction(num1, num2)
   elif option == 3:
      multiplication(num1, num2)
   elif option == 4: 
      division(num1, num2)
   elif option == 0:
      exit()
   else: 
      print("Please choose a valid option")


#-------------------------------------------------------MORE------------------------------------------------------   
elif userchoice == "more": 
   numberlist = more()
   options()
   option_more = int(input("Enter a number between 1-4, or 0 to exit "))

   if option_more == 1: 
      addition_more(numberlist)
   elif option_more == 2:
      subtraction_more(numberlist)
   elif option_more == 3:
      multiplication_more(numberlist)
   elif option_more == 4: 
      division_more(numberlist)
   elif option_more == 0:
      exit()
   else: 
      print("Please choose a valid option")

else:
   print("Choose either two numbers or more.")