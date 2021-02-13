
import pandas as pd
import matplotlib.pyplot as plt
import pp as pre
from tkinter import *
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import fetch_feedback_heart as feed
import fetch_rateus_heart as rateus
import fetch_user_login_details_heart as login
import fetch_user_register_details as register

#C:\\Users\\Lenovo\\Heart_Disease_Prediction_Project\\Dataset.csv



def call_met_user_predict():
    mn_window = Toplevel(frm)
    pre.call_met_predict(mn_window)
    return

def call_met_fetchfeedback():
    mn_window = Toplevel(frm)
    feed.met_fetch_feedback(mn_window)
    return

def call_met_fetchrateus():
    mn_window = Toplevel(frm)
    rateus.met_fetch_rateus(mn_window)
    return

def call_met_user_fetchlogin():
    mn_window = Toplevel(frm)
    login.met_fetch_user_login_details_(mn_window)
    return

def call_met_user_fetchregister():
    mn_window = Toplevel(frm)
    register.met_fetch_user_register_details_(mn_window)
    return










def met_click():
    global df
    
    df =pd.read_csv(txt_path.get())
    print(txt_path.get())
    
    mycolumns=[]
    for col in df.columns:
        mycolumns.append(col)
        
    for item in mycolumns:
         listb.insert("end",item)
       
        
def get_columnsname():
    setvalues=listb.curselection()
    #print(setvalues)
    x = setvalues[0]
    y = setvalues[1]
    
    print(df.iloc[:,x])
    print(" ")
    print(df.iloc[:,y])
    
    x = df.iloc[:,x]
    y = df.iloc[:,y]
    
    #plt.scatter(x,y,c='r') #
    sns.barplot(x,y)  #
    plt.show()
    
    #fig1 = plt.Figure(figsize = (15,15), dpi = 100)
    #ax1 = fig1.add_subplot(111)
    
    #bar1 = FigureCanvasTkAgg(fig1,frm)
    #bar1.get_tk_widget().pack()
    #plt.plot(kind = 'line',ax = ax1)
    

        
        


def met_welcomescreen(fr):
    global txt_path
    global listb
    global frm
    frm = fr
    
    
    lbl_message = Label(frm,text = "Welcome to Heart Disease Predication",foreground='orange',
                        font=('Arial', 24)).pack()
    frm.title("Welcome")
    frm.geometry("800x600")
    
    txt_path = Entry(frm)
    txt_path.pack()
    
    lbl_message = Button(frm,text = "Click here for getting columns ",command = met_click,bg='blue')
    lbl_message.pack() 
    listb = Listbox(frm,selectmode = 'multiple')
    listb.pack()
    lbl_message = Label(frm,text = "Firstly select only 2 valid columns to get a graph between them and Click on Getcolums")
    lbl_message.pack()
    btn_col = Button(frm,text = "Get colmns",command = get_columnsname,bg='blue')
    btn_col.pack()
    btn_col = Button(frm,text = " Lets start prediction",command = call_met_user_predict,bg='blue',font=('Arial', 15),pady=5)
    btn_col.pack()
    btn_col = Button(frm,text = " View Feedback",command = call_met_fetchfeedback,bg='blue',font=('Arial', 15),pady=5)
    btn_col.pack()
    btn_col = Button(frm,text = " View Rating",command = call_met_fetchrateus,bg='blue',font=('Arial', 15),pady=5)
    btn_col.pack()
    btn_col = Button(frm,text = " View user login details",command = call_met_user_fetchlogin,bg='blue',font=('Arial', 15),pady=5)
    btn_col.pack()
    btn_col = Button(frm,text = " View user Register  details",command = call_met_user_fetchregister,bg='blue',font=('Arial', 15),pady=5)
    btn_col.pack()
    
    
    
    return