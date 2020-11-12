import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk,Image 
from datetime import datetime
import ctypes 
import os, sys, time

root = tk.Tk()
root.resizable(False, False)
time1 = ''
root.title("M.H.M.S App")
root.iconbitmap("CS APP\APP_IMAGES\LOGO_ICONS\Icon.ico")
root.unbind_class("Button", "<Key-space>")
# def main_account_screen():
#     global main_screen
header = tk.Label(root, bg='#82C8C4')
header.pack(fill=tk.BOTH, expand=1)
canvas = tk.Canvas(root, width="1040",height="600",relief = tk.FLAT, background = "#C8EBE9")
canvas.pack() 

line = tk.Label(root, width="200",bg='#82C8C4', text="")
canvas.create_window(520,450,window=line)

canvas1 = tk.Canvas(root, width="230",height="230",relief = tk.FLAT, background = "#55B9B3")
canvas.create_window(520,370,window=canvas1)

img4 = ImageTk.PhotoImage(Image.open("CS APP\APP_IMAGES\LOGO_ICONS\CONNECTING_CIRCLE.png")) 
canvas.create_image(-320, 158, anchor=tk.NW, image=img4) 
img2 = ImageTk.PhotoImage(Image.open("CS APP\APP_IMAGES\LOGO_ICONS\dna.png")) 
canvas.create_image(825, -128, anchor=tk.NW, image=img2) 
img3 = ImageTk.PhotoImage(Image.open("CS APP\APP_IMAGES\LOGO_ICONS\dna.png")) 
canvas.create_image(-220, -128, anchor=tk.NW, image=img3) 
img = ImageTk.PhotoImage(Image.open("CS APP\APP_IMAGES\login_images\HMS_TOPPANEL_LOGIN.png"))  
canvas.create_image(20, 20, anchor=tk.NW, image=img) 
img1 = ImageTk.PhotoImage(Image.open("CS APP\APP_IMAGES\LOGO_ICONS\logohead.png")) 
canvas.create_image(470, 170, anchor=tk.NW, image=img1) 
#--------------------------login/Functions----------------------------
def registerbtn():
    global registerbtn
    global canvasRegister
    global usernameRegister
    global passwordRegister
    canvasRegister = tk.Canvas(root, width="220",height="220",relief = tk.FLAT)
    canvas.create_window(520,370,window=canvasRegister)
    #--------------------------Register/Start----------------------------
    usnRegister = tk.Label(root, text="Username")
    canvasRegister.create_window(110,80,window=usnRegister) 

    usernameRegister = tk.Entry(root)
    canvasRegister.create_window(110,100,window=usernameRegister)

    pswRegister = tk.Label(root, text="Password")
    canvasRegister.create_window(110,130,window=pswRegister)
    passwordRegister = tk.Entry(root)
    canvasRegister.create_window(110,170,window=passwordRegister)

    registertxt = tk.Label(root, text="  Register  ", font=("Arial", 26))
    canvasRegister.create_window(110,35,window=registertxt)

    loginReg = tk.Button(root, text ="Register", command = registercommand)
    canvasRegister.create_window(60,200,window=loginReg)  
    registerReg= tk.Button(root, text =" Cancel ", command =  cancelregister)
    canvasRegister.create_window(160,200,window=registerReg)
    #--------------------------Register/End----------------------------
def logincommand():
    global logincommand
    z = username.get()
    x = password.get()
    logusn = open('CS APP/registered_usn.txt','r')
    logpas = open('CS APP/registered_pas.txt','r')
    logusnline = logusn.readline() 
    logpasline = logpas.readline() 
    stripusn = logusnline.split(" ")
    strippas = logpasline.split(" ")

    # with open("registered_accounts.txt") as user:
    #     new = user.readlines()
    #     name = new[0].rstrip()
    #     passw = new[1].rstrip()
    #------Read funct working--------
    # ctypes.windll.user32.MessageBoxW(0, str(strippas), "Tester", 1)
    
    if z in stripusn and x in strippas:
        if  z == '' and x == '':
            ctypes.windll.user32.MessageBoxW(0, "No input", "Login Error", 0)
            return
        elif z == '':
            ctypes.windll.user32.MessageBoxW(0, "No Username", "Login Error", 0)
        elif x == '':
            ctypes.windll.user32.MessageBoxW(0, "No Password", "Login Error", 0)
        else:
            # ctypes.windll.user32.MessageBoxW(0, "Successful", "Login", 0)
            main_ui()
            return
    elif z not in stripusn and x not in strippas:
        ctypes.windll.user32.MessageBoxW(0, "No Account like that has been registered.", "Login",0)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Incorrect Username or Password.", "Login",0)
    return

    
def cancelregister():
    global cancelregister
    canvasRegister.destroy();

def registercommand():
    global registercommand
    c = usernameRegister.get()
    v = passwordRegister.get()
    #----------ERROR ACCEPTING MULTIPLE SPACES------------
    if c == '    ' and v == '    ':
        usernameRegister.delete(0, 'end')
        passwordRegister.delete(0, 'end')
        ctypes.windll.user32.MessageBoxW(0, "No input", "Register Error", 0)
        return
    if c == '   ' and v == '   ':
        usernameRegister.delete(0, 'end')
        passwordRegister.delete(0, 'end')
        ctypes.windll.user32.MessageBoxW(0, "No input", "Register Error", 0)
        return
    if c == '  ' and v == '  ':
        usernameRegister.delete(0, 'end')
        passwordRegister.delete(0, 'end')
        ctypes.windll.user32.MessageBoxW(0, "No input", "Register Error", 0)
        return
    if c == ' ' and v == ' ':
        usernameRegister.delete(0, 'end')
        passwordRegister.delete(0, 'end')
        ctypes.windll.user32.MessageBoxW(0, "No input", "Register Error", 0)
        return
    elif c == '' and v == '':
        ctypes.windll.user32.MessageBoxW(0, "No input", "Register Error", 0)
        return
    else:
        if c == c and v == v:
            readusn = open('CS APP/registered_usn.txt','r')
            readpas = open('CS APP/registered_pas.txt','r')
            readusnline = readusn.readline() 
            readpasline = readpas.readline() 
            stripusnread = readusnline.split(" ")
            strippasread = readpasline.split(" ")

            if len(v) != 4:
                ctypes.windll.user32.MessageBoxW(0, "Password must be 4 digits", "Register", 0)
                return
            elif c in stripusnread and v in strippasread:
                ctypes.windll.user32.MessageBoxW(0, "Account Already Registered", "Register",0)
                return
            else:
                if len(v) == 4:
                    regusn = open('CS APP/registered_usn.txt','a+')
                    regpas = open('CS APP/registered_pas.txt','a+')
                    regusn.write(c + " ")
                    regpas.write(v + " ")
                    regusn.close()
                    regpas.close()
                    ctypes.windll.user32.MessageBoxW(0, "Done! Your Registered", "Register", 0)
                    canvasRegister.destroy();
                    return
def newtimer():
    noww = datetime.now().strftime('   Date: %Y-%m-%d      Time: %H:%M:%S')
    clockk.config(text=noww)
    clockk.after(200, newtimer)
def main_ui():
    global clockk
    global canvapp
    Menus()
    #---------------btnCanvas------------------------------------------
    canvapp = tk.Canvas(root, width="1220",height="1220",relief = tk.FLAT, bg='#82a8C4')
    canvas.create_window(520,370,window=canvapp)

    clockk = tk.Label(root,font=('times', 10, 'bold'), bg='#82a8C4')
    canvas.create_window(890,-3,window=clockk)
    newtimer()

    nameapp = tk.Label(root,font=('times', 10, 'bold'), bg='#82a8C4', text="Medical Health Monitoring System")
    canvas.create_window(120,-3,window=nameapp)

    search = tk.Button(root, text =" Search ", command = Search, width=57,height=2, font=('times', 20, 'bold'))
    canvas.create_window(64,58,window=search)

    librar = tk.Button(root, text ="Sickness Library", command = Symptoms, width=57,height=2, font=('times', 20, 'bold'))
    canvas.create_window(120,150,window=librar)

    logout = tk.Button(root, text =" Logout ", command = Exit, width=57,height=2, font=('times', 20, 'bold'))
    canvas.create_window(64,242,window=logout)
    #---------------btnCanvas------------------------------------------
    canvappsearch = tk.Canvas(root, width="750",height="570",relief = tk.FLAT, background="#C8EBE9")
    canvapp.create_window(710,545,window=canvappsearch)

#---------------btnFunctionsStart------------------------------------------

def Search():
    searchsymp = tk.Label(root, text="Type Symptoms Here", background = "#82C8C4", width="105",height="5", font=('times', 10, 'bold'))
    canvapp.create_window(710,310,window=searchsymp)
    username = tk.Entry(root)
    canvapp.create_window(710,330,window=username)
    searchbtn = tk.Button(root, text ="search", command = "", font=('times', 7, 'bold'))
    canvas.create_window(705,88,window=searchbtn)
    
    scrollvar = tk.Scrollbar(root)
    textfield = tk.Text(root, height=28, width=92)
    canvapp.create_window(710,580,window=scrollvar)
    canvapp.create_window(710,580,window=textfield)

    # canvas.create_window(10,805,window=scrollvar, side=tk.RIGHT, fill=tk.Y)
    # canvas.create_window(10,805,window=textfield, side=tk.LEFT, fill=tk.Y)
    scrollvar.config(command=textfield.yview)
    textfield.config(yscrollcommand=scrollvar.set)
    #----------------this part read and show output--------------------
    quote = """M.H.M.S Search Symptoms."""
    textfield.insert(tk.END, quote)
    #----------------------------end-----------------------------------
def Symptoms():
    canvappsymp = tk.Canvas(root, width="750",height="570",relief = tk.FLAT, background="#C8EBE9")
    canvapp.create_window(710,545,window=canvappsymp)

    labelsym = tk.Label(root,font=('times', 10, 'bold'), bg='#82a8C4', text="Sickness Library", width="105",height="2")
    canvappsymp.create_window(377,30,window=labelsym)
    #----------------this part read and show output--------------------
    scrollsymp = tk.Scrollbar(root)
    textfieldsy = tk.Text(root, height=32, width=92)
    canvappsymp.create_window(377,310,window=scrollsymp)
    canvappsymp.create_window(377,310,window=textfieldsy)
    scrollsymp.config(command=textfieldsy.yview)
    textfieldsy.config(yscrollcommand=scrollsymp.set)

    quote = """M.H.M.S Sickness Library."""
    textfieldsy.insert(tk.END, quote)
    #----------------------------end-----------------------------------
def Exit():
    MsgBox = ctypes.windll.user32.MessageBoxW(0, "are you sure?", "Logging Out", 4)
    if MsgBox == 6:
        sys.exit()
    else:
        pass
#---------------btnFunctionsEnd------------------------------------------

def Menus():
    menu = tk.Menu(root)
    root.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Sickness", command=Sickness)
    filemenu.add_separator()

    helpmenu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About", command=About)
    helpmenu.add_separator()

def Sickness():
    ctypes.windll.user32.MessageBoxW(0, "Insert Sickness here", "Sickness", 0)
def About():
    ctypes.windll.user32.MessageBoxW(0, "This app is for finding sickness by searching symptoms.", "About", 0)

#--------------------------login/FunctionsEnd----------------------------
def ticks():
    now = datetime.now().strftime(' Date: %Y-%m-%d \n Time: %H:%M:%S')
    clock.config(text=now)
    clock.after(200, ticks)
#--------------------------login/begin----------------------------
def start():
    global clock
    global username
    global password
    logintxt = tk.Label(root, text="  Log-In  ", font=("Arial", 26), background = "#55B9B3")
    canvas.create_window(520,290,window=logintxt)

    usn = tk.Label(root, text="           Username           ", background = "#82C8C4")
    canvas.create_window(520,320,window=usn)
    username = tk.Entry(root)
    canvas.create_window(520,340,window=username)

    psw = tk.Label(root, text="            Password           ", background = "#82C8C4")
    canvas.create_window(520,390,window=psw)
    password = tk.Entry(root, show="*")
    canvas.create_window(520,410,window=password)

    login = tk.Button(root, text ="  Login  ", command = logincommand)
    canvas.create_window(470,460,window=login)

    register = tk.Button(root, text ="Register", command =  registerbtn)
    canvas.create_window(570,460,window=register)
#--------------------------login/end----------------------------



    clock = tk.Label(root,font=('times', 20, 'bold'), bg='#C8EBE9')
    canvas.create_window(520,520,window=clock)

    footer = tk.Label(root, bg='#82C8C4', text="Made by TikTokDuo")
    footer.pack(fill=tk.BOTH, expand=1)
    ticks()


start()
root.mainloop()