from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

def met_aboutus(frm):
    global root
    root=frm
    root.geometry("1200x600") 
    root.title(" About Us")

        
    frame_header = ttk.Frame(root)
    frame_header.pack()
    headerlabel = ttk.Label(frame_header, text='ABOUT US', foreground='orange',
                        font=('Arial', 24))
    headerlabel.grid(row=0, column=1)
    messagelabel = ttk.Label(frame_header,
                         text='About our project',
                         foreground='purple', font=('Arial', 10))
    messagelabel.grid(row=1, column=1)
    
    load1 = Image.open("komal.jpg ")
    load1 = load1.resize((250,250),Image.ANTIALIAS)
    render1 = ImageTk.PhotoImage(load1)
    img1  = Label(root,image = render1)
    img1.image = render1
    img1.place(x=  20,y=40)
    
    a= Label(root, text ="Akshara Purwar/1705610016" ) 
    a.place(x = 110, y = 300) 
    
    load2 = Image.open("anushul.jpg ")
    load2 = load2.resize((250,250),Image.ANTIALIAS)
    render2 = ImageTk.PhotoImage(load2)
    img2  = Label(root,image = render2)
    img2.image = render2
    img2.place(x=  250,y=40)
    
    a= Label(root, text ="Anshul kamal/1705610023" ) 
    a.place(x = 300, y = 300) 
    
    load3 = Image.open("ishu.jpg ")
    load3 = load3.resize((250,250),Image.ANTIALIAS)
    render3 = ImageTk.PhotoImage(load3)
    img3  = Label(root,image = render3)
    img3.image = render3
    img3.place(x=  480,y=40)
    
    a= Label(root, text ="Ishu Singh/1705610050" ) 
    a.place(x = 580, y = 300)
    
    a= Label(root, text ="BBDNIIT,LUCKNOW(056)" ) 
    a.place(x = 750, y = 40)
    a= Label(root, text ="CSE,3rdyear" ) 
    a.place(x = 750, y = 70)
    
    a= Label(root, text ="Ishu Singh/1705610050" ) 
    a.place(x = 580, y =70 )
    
    a= Label(root, text ="Ishu Singh/1705610050" ) 
    a.place(x = 580, y = 300)
    
  
    
    
    root.mainloop()
    
    return
    
    