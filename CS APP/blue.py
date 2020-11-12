from tkinter import *
 
def main_account_screen():
    
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Account Login") # set the title of GUI window
 
# create a Form label 
Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 
 
# create Login Button 
Button(text="Login", height="2", width="30").pack() 
Label(text="").pack() 
 
# create a register button
 Button(text="Register", height="2", width="30").pack()
 
main_screen.mainloop() # start the GUI
 
main_account_screen() # call the main_account_screen() function