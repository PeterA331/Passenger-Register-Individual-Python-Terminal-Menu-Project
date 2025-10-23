# Passenger-Register-Individual-Python-Terminal-Menu-Project
Passenger Register – Individual Python Terminal Menu Project:
Developed a terminal-based register system for bus passengers featuring a keyboard-controlled 
menu, data validation, and simple statistics.
Project Details
- Technologies Python standard libraries, modular structure with a main program and a
function module, class-based model for passengers
- Menu and Control Arrow keys for navigation, Enter for selection, clear highlighting of the
current menu item, loops control the program flow
- Data Model Person class with name, age, and gender; lists to store passengers and ages
Features
- Add passenger with step-by-step input and confirmation of name and age
- Print all registered passengers
- Calculate average age with protection against zero-division errors 
- Display position list with gender, two per row for clarity
- Special mode for the 54–56 age range during registration
Robust Input
- Validation of name (letters only), integer requirement for age, buffer flushing to prevent
accidental input, clear error messages 
User Experience
- Terminal clearing, hidden cursor in the menu, pausing and clearing of lines for a clean
return after actions 
Modularity
- Separate file for menus and I/O and a function file for logic, which facilitates testing and
further development

Here is an example runing:

Add a passenger <--
Print all passengers
Take average value of ages   
Show position with gender    
Take passengers between 54-56
Terminate prgram

Enter name for person 1 or enter (0) to undo : Alex
Are you sure of the name:(Alex)
(yes or no)?
yes
Enter age: 32

 are you sure of passenger's age(yes or no)yes
What is the gender of passenger(male or female)?maleee
What is the gender of passenger(male or female)?eale
What is the gender of passenger(male or female)?male
Do you want to add more passengers (yes or no)? yes

Enter name for person 2 or enter (0) to undo : Pamila
Are you sure of the name:(Pamila)
(yes or no)?
no

Enter name for person 2 or enter (0) to undo : 0
Do you want to add more passengers (yes or no)? yes


Add a passenger

Add a passenger

Add a passenger
Print all passengers
Take average value of ages
Show position with gender
Take passengers between 54-56   <--
Terminate prgram

Enter name for person 3 or enter (0) to undo : Tomas
Are you sure of the name:(Tomas)
(yes or no)?
no

Enter name for person 3 or enter (0) to undo : Anders

Add a passenger
Print all passengers    <--  

Add a passenger
Print all passengers
Take average value of ages   
Show position with gender    
Take passengers between 54-56
Terminate prgram
