from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
 


def met_rate_us(frm):
    #lbl_message = Label(frm,text = "RATE US ")
    #lbl_message.pack()
    global root
    root=frm
    root.geometry("500x500") 
    root.title("RATE US")

        
    frame_header = ttk.Frame(root)
    frame_header.pack()
    headerlabel = ttk.Label(frame_header, text='RATE US', foreground='orange',
                        font=('Arial', 24))
    headerlabel.grid(row=0, column=1)
    messagelabel = ttk.Label(frame_header,
                         text='PLEASE RATE US FROM THE SCALE 1 TO 5',
                         foreground='purple', font=('Arial', 10))
    messagelabel.grid(row=1, column=1)

    frame_content = ttk.Frame(root)
    frame_content.pack()
    myvar = StringVar()
    global entry_name
    namelabel = ttk.Label(frame_content, text='ENTER A NO FROM 1-5: ')
    namelabel.grid(row=0, column=0, padx=5, sticky='sw')
    entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
    entry_name.grid(row=1, column=0)
    #
    def clear():
        messagebox.showinfo(title='clear', message='Do you want to clear?')
        entry_name.delete(0, END)
        
    #
    def submit():
        print('Rating:{}'.format(myvar.get()))
        a=format(myvar.get()) #getting input from user

        messagebox.showinfo(title='Submit', message='Thank you for your Rating us.')
        db=pymysql.connect(user="root",password="Pass@123",host="localhost",database="heartdiseaseprediction_db")
        with db:
            mycursor=db.cursor()
            sql="INSERT INTO rate_user_table VALUES(%s)"
            val=(a)
            mycursor.execute(sql,val) ##val value insert in sql
            db.commit()  #commit = 
            print("inserted successfully")
    
        entry_name.delete(0, END)
        
    submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=2, column=0, padx=5,sticky='e')
    clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=2, column=1,padx=5, sticky='w')

    root.mainloop()



    
    


