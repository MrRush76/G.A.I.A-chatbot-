#modules
import sys
import time
import random
import datetime
def calculator():
    #input1 is the variable and "input" means that the string is a question and requires an answer 
    print_slow("Running \"Calculator\"\n")
    time.sleep(2)
    print_slow("Function Loaded.....\n")
    input1 =  input("What service do you require today... 1. Addition 2. Subtraction 3. Multiplication 4. Division \n")
    # the if statements see what input you enters and continues accordingly
    if input1 == "1":
      num1 = input("what is your first number?  ")
      num2 = input("what is your second number?  ")
      print (str(num1) , " + " , str(num2)  , " = " , int(num1)+int(num2))
      # the print value requires int in front of the variable because otherwise it will simply write them next to each other with no space instead of treating them as number values and addind them together
    if input1 == "2":
      num1 = input("what is your first number?  ")
      num2 = input("what is your second number?  ")
      print (int(num1)-int(num2))
    if input1 == "3":
      num1 = input("what is your first number?  ")
      num2 = input("what is your second number?  ")
      print (int(num1)*int(num2))
    if input1 == "4":
      num1 = input("what is your first number?  ")
      num2 = input("what is your second number?  ")
      print (int(num1)/int(num2))
#typing function
def print_slow(str):
  for char in str:
    time.sleep(.00008)
    sys.stdout.write(char)
    sys.stdout.flush()
  return "??\n"
#rock paper scissors
def rockpaperscissors():
  choice = input(print_slow("Lets play Rock Paper Scissors.. You go first.."))
  possible_actions = ["rock", "paper", "scissors"]
  computer_action = random.choice(possible_actions)
  print_slow("You chose " + choice.title() + " Computer chose " +
             computer_action.title() + "\n")
  if computer_action == choice:
    print_slow("Its a tie\n")
  elif choice == "rock":
    if computer_action == "scissors":
      print_slow("Rock smashes scissors! You win!")
    else:
      print("Paper covers rock! You lose.")
  elif choice == "paper" or "Paper":
    if computer_action == "rock":
      print_slow("Paper covers rock! You win!")
    else:
      print_slow("Scissors cuts paper! You lose.")
  elif choice == "scissors" or "Scissors":
    if computer_action == "paper":
      print_slow("Scissors cuts paper! You win!")
    else:
      print_slow("Rock smashes scissors! You lose.")
print_slow("Hello I am G.A.I.A a Virtual Vhatbot created using Python 3\n")
print_slow("I am Capable of perfoming mathematical calculations(1), playing rock paper scissors(2), or displaying the date and time(3) ")
choice = input("What would you like to do? ")
if choice == "1":
    calculator()
elif choice == "2":
    rockpaperscissors()
elif choice == "3":
    print("date and time here:")
else:
    exit()
