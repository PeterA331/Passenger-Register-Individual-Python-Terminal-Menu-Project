#Author:Mhnna Alatallah
#import the file has functions for every choies

import Passenger_functions03

# Import standard libraries for interacting with the operating system, keyboard, and time.
import os
import keyboard
import time


keyToprees=0
# a list that has all choices in the menu
Optionmeny=["Add a passenger\t",#0
            "Print all passengers\t",#1 
            "Take average value of ages\t",#2
            "Show position with gender\t",#3
            "Take passengers between 54-56\t",#4
            "Terminate prgram\t"]#5
# an incremented and decremented variable depended on user's input
#.. in other word, it increments when every time user presses on down arrow..
#.. and decrements when users presses on up arrow
menuSelected=0
# a variable to get input from user, as up arrow, down arrow, Enter 
keyToprees1=0

# This variable acts as a flag to control the program's flow.
# When x is 0, the menu is displayed. When x is 1, the menu display is paused
# to allow other functions to run without being overwritten.
x=0

# --- Main Program Loop ---
# This loop runs indefinitely until the user chooses to exit.
while (True):
    # Clear the terminal screen (works on Windows)
 if x==0:  
    #clear the terminal
    os.system('cls') 
    print("\x1b[?25l")
    # --- Menu Display Logic ---
    # This block of if/elif statements checks the value of 'menuSelected'
    # ..and prints the menu options, adding a "<--" arrow to highlight the current selection.
    # Apperance of meny based on arrow's movment

    if menuSelected==0:
      print(Optionmeny[0] +"<--")
      print(Optionmeny[1])
      print(Optionmeny[2])
      print(Optionmeny[3])
      print(Optionmeny[4])
      print(Optionmeny[5])
    
    elif menuSelected==1:
      print(Optionmeny[0] )
      print(Optionmeny[1]+"<--")
      print(Optionmeny[2])
      print(Optionmeny[3]) 
      print(Optionmeny[4])
      print(Optionmeny[5])

    elif menuSelected==2:
      print(Optionmeny[0] )
      print(Optionmeny[1])
      print(Optionmeny[2]+"<--")
      print(Optionmeny[3])
      print(Optionmeny[4])
      print(Optionmeny[5])
    
    elif menuSelected==3:
      print(Optionmeny[0] )
      print(Optionmeny[1])
      print(Optionmeny[2])
      print(Optionmeny[3]+"<--")  
      print(Optionmeny[4]) 
      print(Optionmeny[5])
    
    elif menuSelected==4:
        print(Optionmeny[0] )
        print(Optionmeny[1])
        print(Optionmeny[2])
        print(Optionmeny[3])
        print(Optionmeny[4]+"<--")
        print(Optionmeny[5])
    else:
      if menuSelected==5: 
        print(Optionmeny[0] )
        print(Optionmeny[1])
        print(Optionmeny[2])
        print(Optionmeny[3])
        print(Optionmeny[4])
        print(Optionmeny[5]+"<--")  

    # This line waits for and reads a single keypress from the user.
    keyPressed = keyboard.read_key()
    # an incremented and decremented variable(menuSelected) depended on user's input
    #.. in other word, it increments when every time user presses on down arrow..
    #.. and decrements when users presses on up arrow
    if keyPressed == "nedpil" and menuSelected + 1 < len(Optionmeny) :
      menuSelected += 1 # Moves the selection down by one.
        
    
    elif keyPressed == "uppil" and menuSelected > 0:
      menuSelected -= 1 # Moves the selection up by one.
    # user chooses one of the choieses on the meny and needs tp press Enter to confirm the choiese
    elif keyPressed == "enter":
      # A small delay to prevent accidental double presses.
      time.sleep(0.100)
      if menuSelected ==0:

        # Set x=1 to pause the menu redraw.
        x=1
        Passenger_functions03.firstChoice()
        #input()
        print("\033[F\033[K", end="")  # ANSI: move cursor up and clear line
        input("press Enter to continue...")
        
        # Set x=0 to allow the menu to be redrawn on the next loop iteration.
        x=0
        
      elif menuSelected ==1:
        x=1
        Passenger_functions03.secondChoice()
        input()
        print("\033[F\033[K", end="")  # ANSI: move cursor up and clear line
        input("press Enter to continue...")
        x=0
      
      elif menuSelected ==2:
        x=1
        Passenger_functions03.thirdChoice()
        input()
        print("\033[F\033[K", end="")  # ANSI: move cursor up and clear line
        input("press Enter to continue...")
        x=0
      
      elif menuSelected ==3:
        x=1
        Passenger_functions03.fourtdChoice()
        input()
        print("\033[F\033[K", end="")  # ANSI: move cursor up and clear line
        input("press Enter to continue...")
        x=0

      elif menuSelected ==4:
        x=1
        
        Passenger_functions03.fifthChoice()
        input()
        print("\033[F\033[K", end="")  # ANSI: move cursor up and clear line
        input("press Enter to continue...")
        x=0  
      
      elif menuSelected ==5:
        # Call the function to end the program.
        Passenger_functions03.EndProgram() 
        # Make the terminal cursor visible again.
        print("\x1b[?25h") 
        break
    # A small delay at the end of each loop iteration to reduce CPU usage.
    time.sleep(0.100) # 0.100 seconds delay               
    

  




