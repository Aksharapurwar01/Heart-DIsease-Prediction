#import tkinter as tk
from tkinter import * 
import pymysql
from tkinter import messagebox
from PIL import Image,ImageTk
def met_user_registerscreen(frm):
   
    
    global root
    root=frm
    #root = Tk()
    root.geometry("1200x600") 
    root.title("USER REGISTERATION PAGE") 
    
######################################################################################    
    def resetact():
        UserID.set("")
        password.set("")
        contact.set("")
        emailid.set("")
        fname.set("")
        lname.set("")
        adress_user.set("")
       
#######################################################################################
    UserID=StringVar()
    password=StringVar()
    contact=StringVar()
    emailid=StringVar()
    fname=StringVar()
    lname=StringVar()
    addressuser=StringVar()
    securityques = StringVar()
    securityans = StringVar()
    
    def submitact():
        userid_user = UserID.get() 
        password_user = password.get() 
        contact_user=contact.get() 
        emailid_user=emailid.get() 
        fname_user=fname.get() 
        lname_user=lname.get() 
        adress_user=addressuser.get()
        security_ques = securityques.get()
        security_ans = securityans.get()
        
        #############
        if userid_user == "":
            
            messagebox.showinfo(title='Warning', message='All fields are required!')
            
        elif password_user == "":
           
            messagebox.showinfo(title='Warning', message='All fields are required!')
            
        elif userid_user == "":
            
            messagebox.showinfo(title='Warning', message='All fields are required!')
            
        elif contact_user == "":
           
            messagebox.showinfo(title='Warning', message='All fields are required!')
        
        elif emailid_user == "":
            
            messagebox.showinfo(title='Warning', message='All fields are required!')
            
        elif fname_user == "":
           
            messagebox.showinfo(title='Warning', message='All fields are required!')
            
        elif lname_user == "":
            
            messagebox.showinfo(title='Warning', message='All fields are required!')
            
        elif adress_user == "":
           
            messagebox.showinfo(title='Warning', message='All fields are required!')    
        
        
        
        
        else:
            messagebox.showinfo(title='Warning', message='Registration successful')
            
            print(f"The details entered by you is {userid_user} {password_user} {contact_user} {emailid_user}{fname_user} {lname_user}  {adress_user}")
        ##################
        db=pymysql.connect(user="root",password="Pass@123",host="localhost",database="heartdiseaseprediction_db")
        #############
        with db: ######
            mycursor=db.cursor() ######
            sql="INSERT INTO register_user_table VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(userid_user,password_user,contact_user,emailid_user,fname_user,lname_user,adress_user,security_ques,security_ans)
            mycursor.execute(sql,val) #######
            db.commit() ######
            print("inserted successfully")
    #################3        
    a= Label(root, text ="User ID-", ) 
    a.place(x = 50, y = 20) 
  
    x =Entry(root,textvar=UserID, width = 35) 
    x.place(x = 150, y = 20, width = 500)
   
    b = Label(root, text ="Password -") 
    b.place(x = 50, y =50 ) 
    
    y = Entry(root, show = "*",textvar=password ,width = 35) 
    y.place(x = 150, y = 50, width = 500) 

    f=Label(root, text ="Contact no -") 
    f.place(x = 50, y = 170) 
    
    v =Entry(root,textvar=contact, width = 35) 
    v.place(x = 150, y = 170, width = 500) 

    e = Label(root, text ="Email ID -") 
    e.place(x = 50, y = 140) 
    
    u=Entry(root,textvar=emailid, width = 35) 
    u.place(x = 150, y = 140, width = 500) 
    

    c = Label(root, text ="Fname-") 
    c.place(x = 50, y = 80) 
    
    z= Entry(root,textvar=fname, width = 35) 
    z.place(x = 150, y = 80, width = 500) 
    
    d = Label(root, text ="Lname-")
    d.place(x = 50, y = 110 ) 
    
    w =Entry(root,textvar=lname, width = 35)
    w.place(x = 150, y = 110, width = 500) 

    
    g= Label(root, text ="Address-")
    g.place(x = 50, y = 200) 
    
    p =Entry(root,textvar=addressuser, width = 35) 
    p.place(x = 150, y = 200, width = 500) 
    
    g= Label(root, text ="Security ques-")
    g.place(x = 50, y = 230) 
    
    p =Entry(root,textvar=securityques, width = 35) 
    p.place(x = 150, y = 230, width = 500) 
    
    g= Label(root, text ="Security ans-")
    g.place(x = 50, y = 260) 
    
    p =Entry(root,textvar=securityans, width = 35) 
    p.place(x = 150, y = 260, width = 500) 






    
    
    btn_submit =Button(root, text ="Submit",  
                      bg ='blue',command=submitact ) 
    btn_submit.place(x = 350, y = 350, width = 75)

    btn_reset =Button(root, text ="RESET",  
                      bg ='blue',command=resetact) 
    btn_reset.place(x = 550, y = 350, width = 75)
    
    load3 = Image.open("thh.jpg ")
    load3 = load3.resize((500,500),Image.ANTIALIAS)
    render3 = ImageTk.PhotoImage(load3)
    img3  = Label(root,image = render3)
    img3.image = render3
    img3.place(x=  680,y=40)
    

    root.mainloop()
    
