import time
import math
import os 

banner = """
                    
 @@@@@@@   @@@@@@   @@@        @@@@@@@  @@@@@@@   @@@ @@@  
@@@@@@@@  @@@@@@@@  @@@       @@@@@@@@  @@@@@@@@  @@@ @@@  
!@@       @@!  @@@  @@!       !@@       @@!  @@@  @@! !@@  
!@!       !@!  @!@  !@!       !@!       !@!  @!@  !@! @!!  
!@!       @!@!@!@!  @!!       !@!       @!@@!@!    !@!@!   
!!!       !!!@!!!!  !!!       !!!       !!@!!!      @!!!   
:!!       !!:  !!!  !!:       :!!       !!:         !!:    
:!:       :!:  !:!   :!:      :!:       :!:         :!:    
 ::: :::  ::   :::   :: ::::   ::: :::   ::          ::    
 :: :: :   :   : :  : :: : :   :: :: :   :           :     
                                                           
"""
# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear') 

print(banner)

center = "Made by Neky"
middle = center.center(50)
print(middle)

center2 = "t.me/mumbus200"
middle2 = center2.center(50)
print(middle2)

center3 = "https://github.com/analyzeCS"
middle3 = center3.center(50)
print(middle3)
print("\n")


list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = ['+' , '-' , '*' , '/']
# Get the first number from user
try:
    the_input = int(input("Enter ur number to calculate: "))
    print("\n")  # New line after first input
    
    # Ask for the operator
    operator = input(f"Choose your operator {list2}: ")
    print("\n")  # New line after operator
    
    if operator not in list2:
        print(f"Invalid operator {list2}")
        os._exit(5)
    
    # Get the second number from user
    second_number = int(input("Enter your second number: "))
    print("\n")  # New line after second input
    
    print("Result:")  
    print("-" * 20)  
    
    # Perform calculation based on selected operator
    if operator == "+":
        result = the_input + second_number
        print(f"{the_input} + {second_number} = {result}")
    
    elif operator == "-":        
        result = the_input - second_number
        print(f"{the_input} - {second_number} = {result}")

    elif operator == "*":
        result = the_input * second_number
        print(f"{the_input} * {second_number} = {result}")

    elif operator == "/":
        if second_number != 0:
            result = the_input / second_number
            print(f"{the_input} / {second_number} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
            
    print("\n")  

    print("Sorry at the moment i can just calculate with +, -, * and / ")

except ValueError:
    print("Please enter a valid number.")
    
time.sleep(1)

print("\n")

# Ask user if they want to continue (y/n) with cursor next to the colon
print("Do you want to calculate something else? (y/n): ", end="")
answer = input().lower()

if answer == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    os.system("python3 mincalc.py")
elif answer == 'n':
    time.sleep(1)
    os._exit(0)


