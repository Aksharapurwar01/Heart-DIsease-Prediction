from tkinter import * 
import pymysql
import welcomee as wel_scn
import pp as pre
from tkinter import messagebox
from PIL import ImageTk,Image


def call_met_welcome():
    mn_window = Toplevel(root)
    wel_scn.met_welcomescreen(mn_window)
    return

def call_met_user_predict():
    mn_window = Toplevel(root)
    pre.call_met_predict(mn_window)
    return





def met_login_user(frm):
    #lbl_message = Label(frm,text = "USER LOGIN PAGE")
    #lbl_message.pack()
    
   
    global root
    root=frm
    
    
    #root = Tk()
    root.geometry("1200x600") 
    root.title("USER LOG IN PAGE") 
    
    UserID=StringVar()
    password=StringVar()
    
    

    def resetact():
        UserID.set("")
        password.set("")
 
    def submitact(): 
        userid_user = UserID.get() 
        password_user = password.get()
        ###########
        if userid_user == "":
            
            messagebox.showinfo(title='Warning', message='All fields are required!')
            
        elif password_user == "":
           
            messagebox.showinfo(title='Warning', message='All fields are required!')
            
                 
            
            
            
        else:
            print(f"The ID entered by you is {userid_user}  and password is {password_user}") 
            logintodb(userid_user, password_user)
        
    def logintodb(userid_user, password_user): 
        global savequery
        db=pymysql.connect(user="root",password="Pass@123",host="localhost",database="heartdiseaseprediction_db")
        cursor = db.cursor() 
        savequery = "select userid_user,password_user from register_user_table"
        checkRec = 0
        try: 
            cursor.execute(savequery) 
            myresult = cursor.fetchall() 
            
            print(userid_user,password_user)
            print("#################################################")
            print("")      
          
            for x in myresult: 
                if x[0] == userid_user and x[1] == password_user:
                    print("Query Excecuted succesfully")
                    checkRec = 1
                    call_met_user_predict()
            if checkRec == 0:
                print("user not found")
          
        except ValueError() as ve:
            print(ve)

    a= Label(root, text ="User ID-", ) 
    a.place(x = 50, y = 20) 
  
    x =Entry(root,textvar=UserID, width = 35) 
    x.place(x = 150, y = 20, width = 200)
   
    b = Label(root,  text ="Password -") 
    b.place(x = 50, y =50 ) 
    
    y = Entry(root, show = "*", textvar=password ,width = 35) 
    y.place(x = 150, y = 50, width = 200) 

    btn_login =Button(root, text ="LOG IN",  
                      bg ='blue',command=submitact) 
    btn_login.place(x = 150, y = 150, width = 75)

    btn_reset =Button(root, text ="RESET",  
                        bg ='blue',command=resetact) 
    btn_reset.place(x = 250, y = 150, width = 75)
    
    load3 = Image.open("th.jpg ")
    load3 = load3.resize((500,500),Image.ANTIALIAS)
    render3 = ImageTk.PhotoImage(load3)
    img3  = Label(root,image = render3)
    img3.image = render3
    img3.place(x=  480,y=40)
    


    root.mainloop() 
 