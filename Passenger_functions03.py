#Author:Mhnna Alatallah
import sys # For system-specific operations like flushing the input buffer

# --- Global Variables ---
# a list to store all the Person objects created.
personlista = [] 
# a list to store the ages of all passengers. 
# it starts with a 0 to avoid index errors on an empty list.
passerngersAge=[0]
# a global flag to indicate if a particular age range should be enforced. 0 = no, 1 = yes.
particularAge=0

# --- Function to clear the keyboard input buffer ---
# This is a cross-platform function to prevent leftover characters (like the 'Enter' key)
# from being accidentally read by the next input() call.
def clear_input_buffer():
    try:
        # Tries the Unix/Linux/macOS method first.
        import termios  # Unix (Linux/Mac)
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    except:
        try:
            # If the Unix method fails, it tries the Windows method.
            import msvcrt  # Windows
            # Keeps reading single characters from the buffer until it's empty.
            while msvcrt.kbhit():
                msvcrt.getch()
        except:
            # If neither method works (e.g., in a non-standard terminal), it does nothing.
            pass

# --- Person Class Definition ---
# A blueprint for creating objects that represent a person.
class Person:
    # The constructor method, called when a new Person object is created.
    def __init__(self, namn, alder, gender):
        # Assigns the provided name and age and gender to the object's attributes.
        self.namn = namn
        self.alder = alder
        self.gender=gender
    # A method to print the person's details in a formatted string.    
    def skriv_ut(self):        # Method
        print(f"{self.namn} är {self.alder} år gammal.")
    
    def showPosition_and_gender(self):
        return self.gender    
        
#---Funtion to check if user is sure about the name of passenger---
def check_NameOfPassenger (SURE_NAME):
    #the user needs to answer with yes or no, otherwise the function iterates
    while(True):
        if(SURE_NAME=="no"):
            SURE_NAME="no"
            return SURE_NAME
            
        elif(SURE_NAME=="yes"):
            SURE_NAME="yes"
            return SURE_NAME
        else:
            print("Pleas (yes or no)\n")  
            clear_input_buffer()
            SURE_NAME=input().lower()

#---Funtion to check if user is sure about the name of passenger---
def check_AgeOfPassenger (SURE_AGE):
    while(True):
        if(SURE_AGE=="no"):
            SURE_AGE="no"
            return SURE_AGE
            
        elif(SURE_AGE=="yes"):
            SURE_AGE="yes"
            return SURE_AGE
        else:
            print("Pleas (yes or no)\n")  
            clear_input_buffer()
            SURE_AGE=input().lower()

# --- Function to handle adding new people (Menu Option 1) ---
def firstChoice():
    
    # Use the global flag to check for special age requirements between(54-56).
    global particularAge

    #Test..If the user wnat to undo the name or age
    sure_name="no"
    sure_age="no"
    gender=" "
    # checks whether the function firstChoise has a custom attribute called indic.
    if not hasattr(firstChoice, "indic"):
        
        #If it doesn't exist, it creates it by doing: firstChoise.indic = 0
        #firstChoise.indic just like a regular variable that remembers its value between function calls
        firstChoice.indic = 0 
    # Variable to control the main loop.
    # The goal is asking user if he/she wants to continue adding new passenger
    Fortsatt = "yes"
    # Loop continues as long as the user wants to add more people
    while Fortsatt == "yes":
        # Reset age for each new person.
           alder=0
        # --- Input loop for the person's name ---
        # This loop will continue until a valid name is entered and confirmed with "yes"
        # The name must be just letters, all other charchters are invaild inclusive numbers
       
           while(sure_name=="no"):
                # Clear any leftover characters from the input buffer,..
                #.. To avoid apperance of previous data.
                clear_input_buffer()
                # Ask user for a name or to enter '0' to cancel.
                namn = input(f"\nEnter name for person {firstChoice.indic + 1} or enter (0) to undo : ")
                # Check if the name contains only alphabetic characters.
                if namn.isalpha():
                    print("Are you sure of the name:({0})".format(namn))
                    clear_input_buffer()
                    sure_name = input(("(yes or no)? \n").lower())
                    
                    sure_name=check_NameOfPassenger(sure_name)
                # Check if the user wants to cancel.
                elif namn=="0":
                    break
                # If the name is not valid, print an error message.
                else:
                    print("Name must contain only letters. Try again.")

        # --- Input loop for the passenger's age ---
        # This loop will continue until an integer age is entered and confirmed with "yes"
           while(sure_age=="no"):
                    # If the user cancelled the name input, also skip the age input.
                    if namn=="0":
                        break
                    else:
                        
                      # Use a try-except block to handle non-integer inputs gracefully
                      
                      try:
                            # Check if the special age restriction is choosed
                            if particularAge==1:
                                # Loop until an age between 54 and 56 is entered.
                               while alder <53 or alder > 56:
                                    clear_input_buffer()
                                    alder = int(input("Enter age: "))
                                    
                                     # Provide a specific error message for the age range.
                                    if alder <53 or alder > 56:
                                        print("The age must be between 54-56 !\n")
                                    else:   
                                        clear_input_buffer()
                                        sure_age=input((" Are you sure of passenger's age(yes or no):\n").lower())   
                                        #check with"yes" or "no" and handel wrong input
                                        sure_age = check_AgeOfPassenger(sure_age)
                                        if(sure_age=="no"):
                                            alder=0
                                            
                                        
                            else:
                                # If there is no special age restriction.
                                clear_input_buffer()
                                alder = int(input("Enter age: "))           
                                clear_input_buffer()
                                sure_age=input(("\n Are you sure of passenger's age(yes or no)").lower() )  
                                #check if user is sure about age of passenger
                                sure_age=check_AgeOfPassenger(sure_age)

                            if(sure_age == "yes"):             
                               # After getting a valid integer, check if it's positive.
                               if alder > 0:
                                   # Add the valid age to the list of ages.
                                   passerngersAge.append(alder)
                                   break # Exit the age loop.
                               else:
                                   print("Age must be a positive number greater than 0.")
                                   sure_age="no"
                                   
                      # If int() fails ( user types "abc" or "54.7"), this block will execute.        
                      except ValueError:
                            print("Invalid input. Age must be an integer.")
                
                # If the user did not cancel the operation.
           if namn!="0":
                while(gender!="male" or gender!="female"):
                      
                      gender=input("What is the gender of passenger(male or female)?").lower()
                      if(gender=="male" or gender=="female"):
                          break
                # Create a new passengers object with the validated name, age and gender.
                person = Person(namn, alder, gender)
                # Add the new object to the main list of passengers.
                personlista.append(person)
                firstChoice.indic += 1  # Keep the counter updated
           # Ask the user if he/she wants to add another person and handel wrong response by while-loop
           # User have to response with "yes" or "no"  
           while(Fortsatt!="yes" or Fortsatt!="no"):
                Fortsatt = input("Do you want to add more passengers (yes or no)? ").lower()
                if (Fortsatt=="yes" or Fortsatt=="no"):
                    break
           # conditions to xheck if the user want to continue adding passengers or not
           # ..reset the special flags for the next loop.
           if Fortsatt=="no":
               particularAge=0
               sure_name="yes"
               sure_age="yes"
           # ..reset the special flags for the next time.
           elif (Fortsatt=="yes"):
               #particularAge=1
               sure_name="no"
               sure_age="no"    


#print all passengers
def secondChoice():
  # check if the length of passerngersAge list is more than 1 
  if len(passerngersAge)<2:
    print("\nNo registered passengers yet !!\n")
        
  else: 
    print("\nRegistered passengers:\n")     
    # Loop through each 'Person' object in the list.
    for p in personlista:
        # Call the object's own print method.
        p.skriv_ut()
    print()

# --- Function to calculate the average age (Menu Option 3) ---
def thirdChoice():
    # Initialize variables for the calculation.
    Value = 0
    counter = -1
    # Loop through the list of ages.
    for i in range(len(passerngersAge)):
        Value += passerngersAge[i] # Sum up all the ages.
        counter += 1 # Count how many ages there are.
    
    # To avoid division by zero if the list is empty (or only has the initial 0).
    if counter > 0:
        mediumValue =(Value / counter)
        print()
        print("Medium value of ages: {0:.3f}".format(mediumValue))
        print()
        return mediumValue
    else:
        return 0  # or handle empty list
    

# --- Function to show gender of passengers by thier positions (Menu Option 4) ---
def fourtdChoice():
    if len(passerngersAge)<2:
       print("\nNo registered passengers yet !!\n")
        
    else: 
        # Show 2 passengers per line
        # --- CORRECTED LOOP ---
        # Iterate through the list with an index using enumerate for cleaner code.
        print()
        for index, p in enumerate(personlista):
            # Prepare the string for the current passenger.
            passenger_info = f"{index + 1}: {p.showPosition_and_gender()}"
            print(f"{passenger_info:<25}", end="") # Print and stay on the same line.

            # If the position number is EVEN, it means we have just printed
            # the 2nd, 4th, 6th, etc., passenger. Time for a new line.
            if (index + 1) % 2 == 0:
                print() # Move to the next line

        print() # Add a final newline for clean output if the list has an odd number of people.

        
# --- Function to add people with a specific age restriction (Menu Option 5) ---
def fifthChoice():
  #Access the global flag.
  global particularAge
  # Set the flag to 1, which will trigger the special age check in firstChoise().
  particularAge=1
  # Call the main function for adding passengers.
  firstChoice()

# --- Function to end the program (Menu Option 6) ---
def EndProgram():
  print("\n Avslutar programmet")
  