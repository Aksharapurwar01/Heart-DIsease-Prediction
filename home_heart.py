# importing only  those functions  
# which are needed 
from tkinter import * 
from tkinter.ttk import *  #####

import user_regis_heart as user_regis
import admin_login_heart as admin

import user_login_heart as user_login
import aboutus_heart as aboutus_
import feeback_heart as feedback_
import mailus_heart as mail_
import rateus_heart as rate_
import call_us as call_
import demo as de
from PIL import Image , ImageTk

def call_user_registerscreen():
    mn_window= Toplevel(root)
    user_regis.met_user_registerscreen(mn_window)
    return

def call_user_admin():
    mn_window= Toplevel(root)
    admin.met_login_admin(mn_window)
    return
#
    

#
def call_userlogin():
    mn_window= Toplevel(root)
    user_login.met_login_user(mn_window)
    return


#
def call_aboutus():
     mn_window= Toplevel(root)
     aboutus_.met_aboutus(mn_window)
     return
#
def call_feedback():
    mn_window= Toplevel(root)
    feedback_.met_feedback(mn_window)
    return

def call_mailus():
    mn_window  = Toplevel(root)
    mail_.met_mail_us(mn_window)
    return
def call_rateus():
    mn_window = Toplevel(root)
    rate_.met_rate_us(mn_window)
    return

def call_callus():
    mn_window = Toplevel(root)
    call_.met_call_us(mn_window)
    return

def call_demo():
    mn_window = Toplevel(root)
    de.met_demo(mn_window)
    return
    
    
    
    
    
# creating tkinter window 
     
if __name__ == '__main__':
    global root
    root = Tk() 
    root.title('HOME PAGE') 
    root.geometry("1200x600")
    
    # Creating Menubar 
    menubar = Menu(root) 
  
    # Adding HOME, LOGIN, ABOUTUS, CONTACT US,FEEDBACK 

    #HOME
    home_page_menu = Menu(menubar, tearoff = 0) ###tearoff==
    menubar.add_command(label ='HOME',command=None) 
    
    #LOG IN
    login_page_menu =Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='LOG IN', menu = login_page_menu) 
    login_page_menu.add_command(label =' ADMIN' , command =  call_user_admin) 
    login_page_menu.add_command(label =' LOGIN' , command =call_userlogin  ) 
    login_page_menu.add_command(label =' REGISTER' , command = call_user_registerscreen)
    login_page_menu.add_separator() ###### ----------
    login_page_menu.add_command(label ='Exit', command = root.destroy)

    #ABOUT US
    aboutus_page_menu = Menu(menubar, tearoff = 0) 
    menubar.add_command(label ='ABOUT US ',command=call_aboutus) 

    #CONTACT US
    contactus_page_menu = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='CONTACT US', menu = contactus_page_menu) 
    contactus_page_menu.add_command(label ='CALL US', command = call_callus) 
    contactus_page_menu.add_command(label ='EMAIL US', command = call_mailus) 
    contactus_page_menu.add_separator() 


    #HELP
    help_page_menu = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='HELP', menu = help_page_menu)  
    help_page_menu.add_command(label ='Demo', command = call_demo) 
    help_page_menu.add_separator() 

    #FEEDBACK
    feedback_page_menu = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='FEEDBACK', menu = feedback_page_menu) 
    feedback_page_menu.add_command(label ='SEND FEEDBACK', command =call_feedback) 

    feedback_page_menu.add_command(label ='RATE US', command = call_rateus) 
    feedback_page_menu.add_separator()
    ##########
    
    
    
    ##################
    load1 = Image.open("heartimage.jpg ")
    load1 = load1.resize((1200,600),Image.ANTIALIAS)
    render1 = ImageTk.PhotoImage(load1)
    img1  = Label(root,image = render1)
    img1.image = render1
    img1.place(x=  0,y=0)
    
    ###########
    
    lbl_message = Label(root,text = "Welcome to Heart Disease Predication",foreground='orange',
                        font=('Arial', 24))
    lbl_message.pack()
   

    # display Menu 
    root.config(menu = menubar) 
    root.mainloop() 