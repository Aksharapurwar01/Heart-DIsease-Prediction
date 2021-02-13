# -*- coding: utf-8 -*-
"""

@author: ishu singh
"""

from tkinter import * 
from tkinter import ttk
import pymysql
#create table user_login_details(user_id text, user_pass text);
def met_fetch_user_register_details_(frm):
    lbl_message = Label(frm,text = "Register DETAILS")
    lbl_message.pack()
    global root
    root=frm
    root.geometry("1200x600") 
    root.title("Register DETAILS")
    root.resizable(False,False)
    
    global tv
    frame1=Frame(root)
    frame1.pack(side=LEFT,padx=20)
    
    
    tv=ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8,9),show="headings")#,height="S"
    tv.pack()
    
    tv.heading(1,text="USER ID")
    tv.heading(2,text="USER PASSWORD")
    tv.heading(3,text ="Contact")
    tv.heading(4,text="Email")
    tv.heading(5,text="First name")
    tv.heading(6,text ="Last Name")
    tv.heading(7,text="Address")
    tv.heading(8,text="Security Ques")
    tv.heading(9,text ="Security Ans")
    btn_reset =Button(root, text ="EXIT",command=frm.destroy).pack()
    
   
    db=pymysql.connect(user="root",password="Pass@123",host="localhost",database="heartdiseaseprediction_db")
    mycursor=db.cursor()
    sql="SELECT * FROM register_user_table"
    mycursor.execute(sql)
    list0=mycursor.fetchall()
    #total=mycursor.rowcount
    #print("TOTAL DATA ENTRIES ARE:",str(total))
    for i in list0:
        tv.insert('','end',values=i)
  
    root.mainloop()
    

    
    



