import MedictateClass
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


#list's

med = MedictateClass.Search
spaceee = ' ' * 33
spaceeee = ' ' * 31
spacee = '\n'
space = '\n' * 3
tt = tk.messagebox.showinfo
fever = ['f', 'e', 'v', 'e', 'r']
headache = 'head ache'
stomachache = 'stomach ache'
stress = 'stress'
colds = 'colds'
a = 'Fever: Drink plenty of fluids to stay hydrated and rest.\n'
b = 'Head Ache: Drink or Give ibuprofen, aspirin, or acetaminophen for pain.\n'
c = 'Stomach Ache: Eat or Serve bland foods, such as saltine crackers.\n'
d = 'Stress: Laughter is the best aid Get some rest.\n'
ff = 'Colds: Keep hydrated and avoid alcohol and caffeine. Keep yourself warm.\n'
e = a + spacee + b + spacee + c + spacee + d + spacee + ff + spacee + "There's More! Coming Soon..."
fp = a + b + c + d + ff

#commands menu
def Sick():
    tk.messagebox.showinfo("Sickness and Remedies", e)
def Sites():
    textt = "mcm.blackboard.com"
    texttt = "www.wikipedia.com"
    textttt = "www.wikihow.com"
    tk.messagebox.showinfo("Sites", textt + '\n' + texttt + '\n' + textttt)
def Save():
    s = bind.get()
    f = open('savesearch.txt', 'a')
    fw = open('history.txt', 'a')
    fww = open('listofremedies.txt', 'w')
    fww.write('-' + a + spacee + '-' + b + spacee + '-' + c + spacee + '-' + d + spacee + '-' + ff + spacee)
    usee = str(bind.get())
    use = str(s)
    fw.write('-' + usee + spacee)
    f.write('-' + use + spacee)
    tk.messagebox.showinfo("Saved", "File Saved you can search it later")
    fww.close()
    fw.close()
    f.close()


def SavedDelete():
    fds = open('savesearch.txt', 'w')
    fds.write('')
    tk.messagebox.showinfo("Saved Search", 'Saved Searches Deleted')
    esa.delete('1.0', 'end')
    rootyx.destroy()
    fds.close()

def SavedMenu():
    global esa
    global rootyx
    rootyx = Tk()
    rootyx.title('Saved')
    rootyx.config(background='maroon')
    rootyx.geometry('{}x{}'.format(400, 400))
    rootyx.resizable(width=TRUE, height=TRUE)
    fa = open('savesearch.txt', 'r')
    fafa = fa.read().replace(' ', '')
    lkf = tk.Frame(rootyx, width=32, height=1, bg='black')
    lkf.grid(row=1, column=4, ipady=28, ipadx=64)
    dsadsaas = Label(rootyx, text='SAVEDFILES MANAGEMENT', width=21, height=3, bg='orange')
    dsadsaas.grid(row=1, column=4)
    dsadsaas = Label(rootyx, width=2, bg='maroon')
    dsadsaas.grid(row=5, column=3)

    scrollbar = Scrollbar(rootyx)
    esa = tk.Text(rootyx, width=40, bd=7, height=10, yscrollcommand=scrollbar.set)
    scrollbar.grid(row=5, column=5, ipady=63, ipadx=1)

    scrollbar.config(command=esa.yview)

    esa.insert("1.0", fafa)
    esa.grid(row=5, column=4)
    b00aa = tk.Button(rootyx, text="Clear Save", height=2, width=10, bd=7, bg='green', command=SavedDelete)
    b00aa.grid(row=7, column=4)
    fa.close()

def HistoryDestroy():
    global rootyxx
    Warning()
    try:
        fd = open('history.txt', 'w')
        fd.write('')
        esaa.delete('1.0', 'end')
        tk.messagebox.showinfo("History", 'History Deleted')
        rootyxx.destroy()
        fd.close()
    except:
        tk.messagebox.showinfo('Cancelled', 'press Ok to continue')
def HistoryMenu():
    global rootyxx
    global esaa
    rootyxx = Tk()
    rootyxx.title('History')
    rootyxx.config(background='maroon')
    rootyxx.geometry('{}x{}'.format(400, 400))
    rootyxx.resizable(width=TRUE, height=TRUE)
    fqq = open('history.txt', 'r')
    fqqq = fqq.read().replace(' ', '')
    lk = tk.Frame(rootyxx, width=20, height=1, bg='black')
    lk.grid(row=1, column=4, ipady=28, ipadx=64)
    dsadsaa = Label(rootyxx, text='HISTORY MANAGEMENT', height=3, bg='orange')
    dsadsaa.grid(row=1, column=4)
    dsadsaa = Label(rootyxx, width=2, bg='maroon')
    dsadsaa.grid(row=5, column=3)

    scrollbarr = Scrollbar(rootyxx)
    esaa = tk.Text(rootyxx, width=40, bd=7, height=10, yscrollcommand=scrollbarr.set)
    scrollbarr.grid(row=5, column=5, ipady=63, ipadx=1)
    scrollbarr.config(command=esaa.yview)
    esaa.insert("1.0", fqqq)
    esaa.grid(row=5, column=4)

    b00a = tk.Button(rootyxx, text="Clear History", height=2, width=10, bd=7, bg='green', command=HistoryDestroy)
    b00a.grid(row=7, column=4)
    fqq.close()
    # = RIGHT, ipadx = 5, padx = 0, ipady = 93, pady = 1 side=RIGHT, ipadx=5, padx=0, ipady=93, pady=1


def Passterisk():
    global userpass
    use = userpass.get()
    userpass.replace(use, '*')

def Email():
    global rooty
    global username
    global userpass
    global userreceiver
    global subject
    global body
    rooty = Tk()
    rooty.title('Email a Friend')
    rooty.config(background='maroon')
    rooty.geometry('{}x{}'.format(500, 770))
    rooty.resizable(width=TRUE, height=TRUE)

    labell = tk.Label(rooty, text='Your Email', bg='orange')
    labell.pack(side=TOP, )
    username = tk.Entry(rooty, width=60, bd=7)
    username.pack(side=TOP, padx=0, pady=20, ipadx=50, ipady=1, )
    label11 = tk.Label(rooty, text='Your Friends Email', bg='orange')
    label11.pack(side=TOP)
    userreceiver = tk.Entry(rooty, width=60, bd=7)
    userreceiver.pack(side=TOP, padx=0, pady=20, ipadx=50, ipady=1, )
    labellll = tk.Label(rooty, text='Password', bg='orange')
    labellll.pack(side=TOP)
    userpass = tk.Entry(rooty, width=60, bd=7,show="*")
    userpass.bind('<KeyRelease>')
    userpass.pack(side=TOP, padx=0, pady=20, ipadx=50, ipady=1)
    labelllll = tk.Label(rooty, text='Subject', bg='orange')
    labelllll.pack(side=TOP)
    subject = tk.Entry(rooty, width=60, bd=7)
    subject.pack(side=TOP, padx=0, pady=20, ipadx=50, ipady=1, )
    labellllll = tk.Label(rooty, text='Body', bg='orange')
    labellllll.pack(side=TOP,)
    body = tk.Text(rooty, width=52, bd=7, height=10)
    body.pack(side=TOP, padx=0, pady=5, ipadx=20, ipady=30)
    b000 = tk.Button(rooty, text="Send", height=3, width=5, bd=7, bg='Green', command=Submit)

    b000.pack(padx=10, pady=10, ipadx=50, ipady=1, side=LEFT)
    b0000 = tk.Button(rooty, text="Clear", height=3, width=5, bd=7, bg='Green', command=EmptyEntrybox)
    b0000.pack(padx=10, pady=10, ipadx=50, ipady=1, side=RIGHT)

def Submit():


    usermail = username.get()
    receivermail = userreceiver.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    pass_word = userpass.get()
    subjectt = subject.get()
    main_message = body.get('1.0', 'end-1c')
    Body = """From: Name here <usermail>
    To: <receivermail>
    Subject:%s 

    %s
    """ %(subjectt, fp+main_message)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(usermail, pass_word)
        server.sendmail(usermail, receivermail, Body)
        tk.messagebox.showinfo('Message Sent', 'Click okay to Continue')
        rooty.destroy()
    except(smtplib.SMTPException, ConnectionRefusedError, OSError):
        tk.messagebox.showinfo('Message Not Sent', 'Click okay to Retry')
    finally:
        server.close()

def About():
    tk.messagebox.showinfo("About", "Helping the people to know the\nremedies to a specific sickness")
def Use():
    tk.messagebox.showinfo("How to use", "Search any common sickness in the search bar\nand you will see the remedies in the\nListbox\nMore Options and Remedies coming soon!")

def EmptyTextbox():
    fw = open('history.txt', 'a')
    usee = str(bind.get())
    fw.write('-' + usee + spacee)
    fw.close()
    bind.delete(0, 'end')
    list2.delete(0, 'end')
    return
def EmptyEntrybox():
    username.delete(0, 'end')
    userpass.delete(0, 'end')
    userreceiver.delete(0, 'end')
    subject.delete(0, 'end')
    body.delete(1.0, 'end')
    return
def Exit():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')

def search_command2(event=None):
    x = e1.get().lower()
    list2.delete(0, 'end')

    if x:
        for word in a, b, c, d, ff:
            if word.lower().startswith(x):
                list2.insert('end', word)

#start
roots = Tk()
roots.title("MEDICTATE_Prototype")
roots.config(background = 'maroon')
roots.geometry('{}x{}'.format(700, 820))
roots.resizable(width=TRUE, height=TRUE)

image000 = ImageTk.PhotoImage(file='START.png')

b0 = tk.Button(text="START", height=60, width=80, bd=7, bg='green', image=image000, command=roots.destroy)
b0.grid(row=6, column=2, pady=100, padx=10, columnspan=205)

image0 = ImageTk.PhotoImage(file='g1.png')
image_e = tk.Label(roots, compound=tk.TOP, highlightthickness=5, borderwidth=0, image=image0, bg='maroon').grid(row=2, column=2, columnspan=10, ipady=160, ipadx=50)
roots.mainloop()

root = Tk()
root.title("MEDICTATE_Prototype")
root.config(background ='maroon')
root.geometry('{}x{}'.format(700, 800))
root.resizable(width=FALSE, height=FALSE)

#picture's
image2 = ImageTk.PhotoImage(file="g2.png")
image3 = ImageTk.PhotoImage(file="g3.png")

l1 = tk.Label(root, text='',  bg='maroon')
l1.pack()
l2 = tk.Label(root, text=space,  bg='maroon')
l2.pack()

image_2 = tk.Label(root, compound=tk.CENTER, image=image2, bg='maroon').pack(side="top")

#main
title_text = tk.StringVar()

e1 = tk.Entry(root, textvariable=title_text, width=80, bd=5)
e1.pack()
bind = e1
binds = bind.lower()
bind.bind('<KeyRelease>', search_command2)
bind.insert("0", spaceee + spaceee + "-Search it here-")

l33 = tk.Label(root, text='',  bg='maroon')
l33.pack()

l3 = tk.Label(root, image=image3,  bg='maroon')
l3.pack(ipadx=5, padx=103)

l3e = tk.Label(root, text='\n',  bg='maroon')
l33.pack()

list2 = tk.Listbox(root, height=10, width=80, bd=5)
list22 = list2
list2.pack()
list2.insert("0", spaceeee + spaceeee + "-Press Clear to Start-")

l3 = tk.Label(root, text='',  bg='maroon')
l3.pack()

def Buttons():
    #rooty-email

    b1 = tk.Button(root, text="Clear", width=12, bd=7, bg='red', command=EmptyTextbox)
    b1.pack(padx=120, pady=0, ipadx=10, ipady=5, side =RIGHT)

    b2 = tk.Button(root, text="Email Remedies", width=12, bd=7, bg='green', command=Email)
    b2.pack(padx=5, pady=1, ipadx=1, ipady=5, side=RIGHT)

    b2 = tk.Button(root, text="Save Search", width=12, bd=7, bg='green', command=Save)
    b2.pack(padx=5, pady=1, ipadx=1, ipady=5, side=RIGHT)
def Menus():
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Sickness", command=Sick)
    filemenu.add_command(label="Useful Sites", command=Sites)
    filemenu.add_separator()
    filemenu.add_command(label="Saved", command=SavedMenu)
    filemenu.add_separator()
    filemenu.add_command(label="History", command=HistoryMenu)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=Exit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)
    helpmenu.add_command(label="How to use", command=Use)


Buttons()
Menus()
mainloop()