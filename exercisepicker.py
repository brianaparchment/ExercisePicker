#This program allows users to select exercises from a csv file
#Read csv file into program
import csv
import random


file_name = "ExercisePicker/Exercises.csv"


#opens csv file
with open(file_name, newline='') as file_csv:
    read = csv.reader(file_csv, delimiter=',')
    name_list = [] #Empty list to store exc names
    descr_list = [] #Empty list to store exc descriptions
    
    for column in read:
        name = column[0]
        descr = column[1]
        
        #Content in csv file is added to the lists
        name_list.append(name)
        descr_list.append(descr)
        
        #Dictionary to store exc names and descriptions
        exc_dict = dict(zip(name_list, descr_list))
        
    #Convert dictionary into list of tuples
    content_list = list(exc_dict.items())
    
    random_exc = random.choice(content_list)

    #Converts a shallow copy of list
    copy_list = content_list

#Completed exercise list
completed_exc = []


ran_name = random.choice(name_list)
ran_exc = random.choice(content_list)



    
class Exercises:
    
      
    #Method to display exc name
    def display_name(self):     
        print(ran_name)
        update_name()
        
    
    #Method to display name and description
    def display_descr(self):
        print(ran_exc)
        update_content()
       
                 
fc = Exercises()
#fc.display_name()
#fc.display_descr()

def quit_func():
    user_quit = input("Press 'Q' to quit")
    user_quit = user_quit.upper()
    if(user_quit == "Q"): 
        quit()                       
 
 
def search_dict():
    search = input("Enter the name of the exercise: ")
    
    for i in search:
        if(search == "Exc 1"):
            dict_key = content_list[0]
            print(dict_key)
            
        if(search == "Exc 2"):
            dict_key = content_list[1]
            print(dict_key)
            
        if(search == "Exc 3"):
            dict_key = content_list[2]
            print(dict_key)
            
        if(search == "Exc 4"):
            dict_key = content_list[3]
            print(dict_key)
            
        if(search == "Exc 5"):
            dict_key = content_list[4]
            print(dict_key)
            
        if(search == "Exc 6"):
            dict_key = content_list[5]
            print(dict_key)
            
        if(search == "Exc 7"):
            dict_key = content_list[6]
            print(dict_key)
            
        else:
            print("This exercise does not exist")
            menu()
    
    
#Updates name list if exercise name is selected
def update_name():
    #Ask user if they want to select this exercise name
    name_choice = input("Would you like to select this exercise? (Enter 'Y' for yes and 'N' for no): ")
    name_choice = name_choice.upper()
    for i in name_choice:
        #If user selectes Y for yes the program continues
        if (name_choice == "Y"):
            #Removes exercise from list
            name_list.remove(ran_name)
            completed_exc.append(ran_name)
            
        if (name_choice == "N"):
            new_exc()
        
        

#Updates content list if exercise is selected   
def update_content():
    #Ask user if they want to select this exercise
    exc_choice = input("Would you like to select this exercise? (Enter 'Y' for yes and 'N' for no): ")
    exc_choice = exc_choice.upper()
    for i in exc_choice:
        #If user selectes Y for yes the program continues
        if (exc_choice == "Y"):
            content_list.remove(ran_exc)
            completed_exc.append(ran_exc)
            
        if (exc_choice == "N"):
            new_exc()
        


   
   
def new_exc():
    #Make user interface
    #Allow user to get new exercise
    new_exercise = input("Press Enter to get a new exercise")
    
    user_display = input("Enter 'name' to view the exercise name or Enter 'both' to view the exercise name and description: ")
    user_display = user_display.upper()
    if(user_display == "NAME"):
        fc.display_name()
    if(user_display == "BOTH"):
        fc.display_descr()

    

   
    
def menu():
    options = ["L: Look up an exercise", "N: Get a new exercise", "H: Help", "Q:Quit"]
    
    display_options = input("Press 'M' to display menu: ")
    display_options.upper()
    if (display_options == "M"):
        print(options)
        
    user_option = input("What would you like to do? Enter 'L', 'N', 'H', 'Q': ")
    user_option = user_option.upper()
    if (user_option == "L"):
        search_dict()
        
    if (user_option == "N"):
        new_exc()
        
    if(user_option == "Q"):
        quit_func()
        
    if(user_option == "H"):
        menu()
         
menu()   



       
       

