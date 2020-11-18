import tkinter as tk
from tkinter import filedialog, Text
from tkinter.constants import DISABLED
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

def canceladmin():
    global canvasAdmin
    canvasAdmin.destroy();
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


#------------------------NOT YET WORKING(ADMIN ADD DELETE)---------------------------------------

def save_button():
    global readsickadddel
    entries = textfieldsyadminadddel.get()
    readsickadddel = open('CS APP/sickness.txt','a+')
    readsickadddel.write(entries)
    readsickadddel.close()
    ctypes.windll.user32.MessageBoxW(0, "Done, Changes Saved!", "ADD", 0)
    return
def add_delete_sick():
    global textfieldsyadminadddel
    canvasadminadddel = tk.Canvas(root, width="750",height="570",relief = tk.FLAT, background="#C8EBE9")
    canvappadmin.create_window(710,545,window=canvasadminadddel)

    labeladminadddel = tk.Label(root,font=('times', 10, 'bold'), bg='#82a8C4', text="Sickness Add/Delete", width="105",height="2")
    canvasadminadddel.create_window(377,30,window=labeladminadddel)
    #----------------this part read and show output--------------------


    scrolladminadddel = tk.Scrollbar(root)
    textfieldsyadminadddel = tk.Text(root, height=23, width=92)
    canvasadminadddel.create_window(377,315,window=scrolladminadddel)
    canvasadminadddel.create_window(377,315,window=textfieldsyadminadddel)
    scrolladminadddel.config(command=textfieldsyadminadddel.yview)
    textfieldsyadminadddel.config(yscrollcommand=scrolladminadddel.set)

    textfieldsyadminadddell = tk.Text(root, height=5, width=92)
    canvasadminadddel.create_window(377,80,window=textfieldsyadminadddell)
    quotee = """M.H.M.S Add/Delete Sickness (Follow the Format)."""
    showreadd = quotee + "\n" + "Sickness_Name - (1stSymptom, 2nd, 3rd, 4th) 'Definition'"
    textfieldsyadminadddell.insert(tk.END, showreadd)
    textfieldsyadminadddell.config(state=DISABLED)

    add = tk.Button(root, text ="  Save  ", command = save_button, width=10,height=1, font=('times', 15, 'bold'))
    canvasadminadddel.create_window(80,540,window=add)



def show_sick():
    canvasadminsymp = tk.Canvas(root, width="750",height="570",relief = tk.FLAT, background="#C8EBE9")
    canvappadmin.create_window(710,545,window=canvasadminsymp)

    labeladminsym = tk.Label(root,font=('times', 10, 'bold'), bg='#82a8C4', text="Sickness Library", width="105",height="2")
    canvasadminsymp.create_window(377,30,window=labeladminsym)
    #----------------this part read and show output--------------------
    scrolladminsymp = tk.Scrollbar(root)
    textfieldsyadmin = tk.Text(root, height=32, width=92)
    canvasadminsymp.create_window(377,310,window=scrolladminsymp)
    canvasadminsymp.create_window(377,310,window=textfieldsyadmin)
    scrolladminsymp.config(command=textfieldsyadmin.yview)
    textfieldsyadmin.config(yscrollcommand=scrolladminsymp.set)

    readsick = open('CS APP/sickness.txt','r')
    readsicknes = readsick.read() 
    quote = """M.H.M.S Sickness Library."""
    showread = quote + "\n" + readsicknes
    textfieldsyadmin.insert(tk.END, showread)
    textfieldsyadmin.config(state=DISABLED)

def admin_main():
    global clockkk
    global canvappadmin
    root.title("M.H.M.S --ADMIN--")
    Menus()
    #---------------btnCanvas------------------------------------------
    canvappadmin = tk.Canvas(root, width="1220",height="1220",relief = tk.FLAT, bg='#82a8C4')
    canvas.create_window(520,370,window=canvappadmin)

    clockkk = tk.Label(root,font=('times', 10, 'bold'), bg='#82a8C4')
    canvas.create_window(890,-3,window=clockkk)
    adminticks()

    nameappadmin = tk.Label(root,font=('times', 10, 'bold'), bg='#82a8C4', text="Medical Health Monitoring System")
    canvas.create_window(120,-3,window=nameappadmin)

    nameappadministrator = tk.Label(root,font=('times', 15, 'bold'), bg='#82a8C4', text="Administrator")
    canvas.create_window(520,-3,window=nameappadministrator)

    searchadmin = tk.Button(root, text =" Sickness ", command = show_sick, width=57,height=2, font=('times', 20, 'bold'))
    canvas.create_window(70,58,window=searchadmin)

    libraradmin = tk.Button(root, text =" Add/Delete", command = add_delete_sick, width=57,height=2, font=('times', 20, 'bold'))
    canvas.create_window(80,150,window=libraradmin)

    logoutadmin = tk.Button(root, text =" Log-out ", command = Exit, width=57,height=2, font=('times', 20, 'bold'))
    canvas.create_window(64,242,window=logoutadmin)

    #---------------btnCanvas------------------------------------------
    canvappsearchadmin = tk.Canvas(root, width="750",height="570",relief = tk.FLAT, background="#C8EBE9")
    canvappadmin.create_window(710,545,window=canvappsearchadmin)


#---------------btnFunctionsStart------------------------------------------
def search_command2(event=None):
    x = searchsick.get()
    textfield.delete(0, 'end')

    if x:
        findsick = open('CS APP/sickness.txt','r')
        findsickline = findsick.read()
        for word in findsickline:
            if word.startswith(x):
                textfield.insert('end', word)
def Search():
    global textfield
    global searchsick
    searchsymp = tk.Label(root, text="Type Symptoms Here", background = "#82C8C4", width="105",height="5", font=('times', 10, 'bold'))
    canvapp.create_window(710,310,window=searchsymp)

#-----------------searchtype start---------------------
    searchsick = tk.Entry(root)
    bind = searchsick
    bind.bind('<KeyRelease>', search_command2)
    canvapp.create_window(710,330,window=searchsick)
#-----------------searchtype end---------------------


    searchbtn = tk.Button(root, text ="search", command = "", font=('times', 7, 'bold'))
    canvas.create_window(705,88,window=searchbtn)
    

    textfield = tk.Listbox(root, height=28, width=123)
    canvapp.create_window(710,570,window=textfield)

    #----------------this part read and show output--------------------
    quote = """M.H.M.S Search Symptoms."""
    textfield.insert(tk.END, quote)
    textfield.config(state=DISABLED)

    #----------------------------end-----------------------------------
def Symptoms():
    canvappsymp = tk.Canvas(root, width="750",height="570",relief = tk.FLAT, background="#C8EBE9")
    canvapp.create_window(710,545,window=canvappsymp)

    labelsym = tk.Label(root,font=('times', 10, 'bold'), bg='#82a8C4', text="Sickness Library", width="105",height="2")
    canvappsymp.create_window(377,30,window=labelsym)
    #----------------this part read and show output--------------------
    readsick = open('CS APP/sickness.txt','r')
    readsickline = readsick.read() 

    scrollsymp = tk.Scrollbar(root)
    textfieldsy = tk.Text(root, height=32, width=92)
    canvappsymp.create_window(377,310,window=scrollsymp)
    canvappsymp.create_window(377,310,window=textfieldsy)
    scrollsymp.config(command=textfieldsy.yview)
    textfieldsy.config(yscrollcommand=scrollsymp.set)

    quote = """M.H.M.S Sickness Library."""
    textfieldsy.insert(tk.END, quote +"\n"+readsickline)
    textfieldsy.config(state=DISABLED)

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
def AdminLogin():
    adminz = usernameadmin.get()
    adminx = passwordadmin.get()
    logusnadmin = open('CS APP/admin_usn.txt','r')
    logpasadmin = open('CS APP/admin_pass.txt','r')
    logusnlineadmin = logusnadmin.readline() 
    logpaslineadmin = logpasadmin.readline() 
    stripusn = logusnlineadmin.split(" ")
    strippas = logpaslineadmin.split(" ")

    if adminz in stripusn and adminx in strippas:
        if  adminz == '' and adminx == '':
            ctypes.windll.user32.MessageBoxW(0, "No input", "Login Error", 0)
            return
        elif adminz == '':
            ctypes.windll.user32.MessageBoxW(0, "No Username", "Login Error", 0)
        elif adminx == '':
            ctypes.windll.user32.MessageBoxW(0, "No Password", "Login Error", 0)
        else:
            admin_main()
            return
    elif adminz not in stripusn and adminx not in strippas:
        ctypes.windll.user32.MessageBoxW(0, "No Account like that has been registered.", "Login",0)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Incorrect Username or Password.", "Login",0)
        return

def Admin():
    global canvasAdmin
    global usernameadmin
    global passwordadmin

    canvasAdmin = tk.Canvas(root, width="220",height="220",relief = tk.FLAT)
    canvas.create_window(520,370,window=canvasAdmin)
    #--------------------------Register/Start----------------------------
    usnadmin = tk.Label(root, text="Username")
    canvasAdmin.create_window(110,80,window=usnadmin) 

    usernameadmin = tk.Entry(root)
    canvasAdmin.create_window(110,100,window=usernameadmin)

    passadmin = tk.Label(root, text="Password")
    canvasAdmin.create_window(110,130,window=passadmin)
    passwordadmin = tk.Entry(root)
    canvasAdmin.create_window(110,170,window=passwordadmin)

    admintxt = tk.Label(root, text="  ADMIN  ", font=("Arial", 26))
    canvasAdmin.create_window(110,35,window=admintxt)

    adminlogin = tk.Button(root, text ="Log-in", command = AdminLogin)
    canvasAdmin.create_window(60,200,window=adminlogin)  
    admincancel= tk.Button(root, text =" Cancel ", command =  canceladmin)
    canvasAdmin.create_window(160,200,window=admincancel)


#--------------------------login/FunctionsEnd----------------------------
def ticks():
    now = datetime.now().strftime(' Date: %Y-%m-%d \n Time: %H:%M:%S')
    clock.config(text=now)
    clock.after(200, ticks)
def adminticks():
    nowww = datetime.now().strftime(' Date: %Y-%m-%d \n Time: %H:%M:%S')
    clockkk.config(text=nowww)
    clockkk.after(200, adminticks)
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

    admin = tk.Button(root, text ="Admin", command =  Admin)
    canvas.create_window(1018,590,window=admin)

    
#--------------------------login/end----------------------------



    clock = tk.Label(root,font=('times', 20, 'bold'), bg='#C8EBE9')
    canvas.create_window(520,520,window=clock)

    footer = tk.Label(root, bg='#82C8C4', text="Made by TikTokDuo")
    footer.pack(fill=tk.BOTH, expand=1)
    ticks()


start()
root.mainloop()