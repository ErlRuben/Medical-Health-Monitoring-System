import tkinter as tk
from tkinter import filedialog, Text
# from PIL import ImageTk,Image 
import os

root = tk.Tk()
class GUI():
    def click():
        print("pressed")

    canvas = tk.Canvas(root, width="900",height="600",relief = tk.FLAT, background = "#D2D2D2")
    canvas.pack() 
    
    #button 
    buttonBG = canvas.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
    buttonTXT = canvas.create_text(50, 15, text="Log-in")
    canvas.tag_bind(buttonBG, "<Button-1>", click)
    
    #image
    # img = ImageTk.PhotoImage(Image.open("ball.png"))  
    # canvas.create_image(20, 20, anchor=NW, image=img) 

    e1 = tk.Entry(canvas)
    canvas.create_window(100,10,window=e1)

    
root.mainloop()


