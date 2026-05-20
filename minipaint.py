from tkinter import *
from PIL import ImageTk, Image
vent= Tk()
vent.title("trabajar en el lienzo usando funciones")
vent.geometry("600x600")

Label=Label(vent,text="ingresa un color :")
Label.place(relx=0.6,rely=0.9,anchor= CENTER)

input_box= Entry(vent)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.9,anchor= CENTER)

canvas= Canvas(vent, width=580,height=550,bg="white", highlightbackground="lightgray")
canvas.pack()
img= ImageTk.PhotoImage(Image.open("start_point.png"))
my_image = canvas.create_image(50,50,image=img)

direction = ""
oldx=50
oldy=50
mewx=50
mewy=50

def right_dir(event):
    global direction
    global oldx
    global oldy
    global mewx
    global mewy
    
    oldx = mewx
    oldy = mewy
    
    mewx = mewx + 10
    direction = "right"
    
    draw(direction,oldx,oldy,mewx,mewy)

def down_dir(event):
    global direction
    global oldx
    global oldy
    global mewx
    global mewy
    
    oldx = mewx
    oldy = mewy
    
    mewy = mewy + 10
    direction = "down"
    
    draw(direction,oldx,oldy,mewx,mewy)

def left_dir(event):
    global direction
    global oldx
    global oldy
    global mewx
    global mewy
    
    oldx = mewx
    oldy = mewy
    
    mewx = mewx - 10
    direction = "left"
    
    draw(direction,oldx,oldy,mewx,mewy)

def up_dir(event):
    global direction
    global oldx
    global oldy
    global mewx
    global mewy
    
    oldx = mewx
    oldy = mewy
    
    mewy = mewy - 10
    direction = "up"
    
    draw(direction,oldx,oldy,mewx,mewy)

def draw(direction, oldx,oldy,mewx,mewy):
    fill_color = input_box.get()
    
    if(direction=="right"):
        right_line= canvas.create_line(oldx,oldy,mewx,mewy,width= 3,fill=fill_color)
    if(direction=="down"):
        right_line= canvas.create_line(oldx,oldy,mewx,mewy,width= 3,fill=fill_color)
    if(direction=="left"):
        right_line= canvas.create_line(oldx,oldy,mewx,mewy,width= 3,fill=fill_color)
    if(direction=="up"):
        right_line= canvas.create_line(oldx,oldy,mewx,mewy,width= 3,fill=fill_color)




canvas.pack()
vent.bind("<Right>",right_dir)
vent.bind("<Down>",down_dir)
vent.bind("<Left>",left_dir)
vent.bind("<Up>",up_dir)

vent.mainloop()