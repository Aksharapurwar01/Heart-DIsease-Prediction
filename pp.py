# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 16:59:38 2020

@author: Lenovo
"""
from tkinter import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %matplotlib inline

# Other libraries
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler

# Machine Learning
from sklearn.neighbors import KNeighborsClassifier



    

def takeInput():
    #####
    
    ######
    
    inputValues = []
    age1 = ((int(age.get()) - 29)  / (77-29 ))
    print(age1)
    trestbps1 = ((int(rbp.get()) - 94)/(200-94))
    chol1 = ((int (serumChol.get()) - 126)/(564-126))
    thalach1 = ((int(thalach.get()) - 71)/(202-71))
    oldpeak1 = (float(oldpeak.get())/ (6.2))

    inputValues.append(age1)
    inputValues.append(sex.get())
    inputValues.append(chestPain.get())
    inputValues.append(trestbps1)
    inputValues.append(chol1)
    inputValues.append(FBS.get())
    inputValues.append(ECG.get())
    inputValues.append(thalach1)
    inputValues.append(trestbps1)
    inputValues.append(oldpeak1)
    inputValues.append(slope.get())
    inputValues.append(ca.get())
    inputValues.append(thal.get()) 

    print(inputValues)


    print("\n") 
    final_Result = knn_classifier.predict([inputValues])
    print(final_Result)


    mainWindow1 = Toplevel(mainWindow)
    mainWindow1.geometry('800x600')
    mainWindow1.title("RESULT PREDICTION")
    
    ##############

    mainWindow1.columnconfigure(0, weight=2)
    mainWindow1.columnconfigure(1, weight=1)
    mainWindow1.columnconfigure(2, weight=2)
    mainWindow1.columnconfigure(3, weight=2)
    mainWindow1.rowconfigure(0, weight=1)
    mainWindow1.rowconfigure(1, weight=10)
    mainWindow1.rowconfigure(2, weight=10)
    mainWindow1.rowconfigure(3, weight=1)
    mainWindow1.rowconfigure(4, weight=1)
    mainWindow1.rowconfigure(5, weight=1)
    
    ############

    if final_Result[0] == 1:
        label1 = Label(mainWindow1, text="HEART DISEASE DETECTED",font=('Arial', 20), fg='purple')
        label1.grid(row=0, column=1, columnspan=6)
        label2 = Label(mainWindow1, text="PLEASE VISIT NEAREST CARDIOLOGIST AT THE EARLIEST",font=('Arial', 10), fg='red')
        label2.grid(row=1, column=1, columnspan=6)
        
    else:
        label1 = Label(mainWindow1, text="NO DETECTIOIN OF HEART DISEASES", font=('Arial', 20))
        label1.grid(row=0, column=1, columnspan=6)
        label2 = Label(mainWindow1, text="Do not forget to exercise daily. ",font=('Arial', 10), fg='green')
        label2.grid(row=1, column=1, columnspan=6)      
    return
        


heart = pd.read_csv("C:\\Users\\Lenovo\\Heart_Disease_Prediction_Project\\Dataset.csv")
# we have unknown values '?'
# change unrecognized value '?' into mean value through the column
############## min max scaler
min_max = MinMaxScaler()
columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
heart[columns_to_scale ] = min_max.fit_transform(heart[columns_to_scale])
#############min max scaler
y = heart['target']
X = heart.drop(['target'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)




# print(len(X_train))
# len(X_test)
knn_classifier = KNeighborsClassifier(n_neighbors = 4)
knn_classifier.fit(X_train, y_train)


def call_met_predict(fr):
    global mainWindow
    global age
    global sex
    global chestPain
    global rbp
    global serumChol
    global FBS
    global ECG
    global thalach
    global exang
    global oldpeak
    global slope
    global ca
    global thal
    mainWindow = fr
    
  
    
    
    
    mainWindow.geometry('800x600')
    mainWindow['padx']=20
    mainWindow.title("HEART DISEASE PREDICTION")

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=1)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=2)
    mainWindow.rowconfigure(0, weight=0)
    mainWindow.rowconfigure(1, weight=0)
    mainWindow.rowconfigure(2, weight=1)
    mainWindow.rowconfigure(3, weight=1)
    mainWindow.rowconfigure(4, weight=1)
    mainWindow.rowconfigure(5, weight=1)
    mainWindow.rowconfigure(6, weight=1)
    mainWindow.rowconfigure(7, weight=1)
    mainWindow.rowconfigure(8, weight=10)


    label1 = Label(mainWindow, text="HEART DISEASE PREDICTION MODEL", font=('Arial', 20), fg='orange')
    label1.grid(row=0, column=0, columnspan=6)

    label2 = Label(mainWindow, text="Enter the details carefully", font=('Arial', 10) , fg='purple' )
    label2.grid(row=1, column=0, columnspan=6)


#frame for the feature inputs
    ageFrame = LabelFrame(mainWindow, text="Age(yrs)")
    ageFrame.grid(row=2, column=0)
    ageFrame.config(font=("Arial", 15))
    age= Entry(ageFrame)
    age.grid(row=2, column=2, sticky='nw')

    sexFrame = LabelFrame(mainWindow, text="Gender (0-F,1-M)")
    sexFrame.grid(row=2, column=1)
    sexFrame.config(font=("Arial", 15))
    sex= Entry(sexFrame)
    sex.grid(row=2, column=2, sticky='nw')

    chestPainFrame = LabelFrame(mainWindow, text="ChestPain (0-4)")
    chestPainFrame.grid(row=2, column=2)
    chestPainFrame.config(font=("Arial", 15))
    chestPain= Entry(chestPainFrame)
    chestPain.grid(row=2, column=2, sticky='nw')


    rbpFrame = LabelFrame(mainWindow, text="RBP (94-200)")
    rbpFrame.grid(row=3, column=0)
    rbpFrame.config(font=("Arial", 15))
    rbp= Entry(rbpFrame)
    rbp.grid(row=2, column=2, sticky='nw')

    serumCholFrame = LabelFrame(mainWindow, text="Serum Chol")
    serumCholFrame.grid(row=3, column=1)
    serumCholFrame.config(font=("Arial", 15))
    serumChol = Entry(serumCholFrame)
    serumChol.grid(row=2, column=2, sticky='n')

    FBSFrame = LabelFrame(mainWindow, text="Fasting BP(0-4)")
    FBSFrame.grid(row=3, column=2)
    FBSFrame.config(font=("Arial", 15))
    FBS= Entry(FBSFrame)
    FBS.grid(row=2, column=2, sticky='nw')

    ECGFrame = LabelFrame(mainWindow, text="ECG (0,1,2)")
    ECGFrame.grid(row=4, column=0)
    ECGFrame.config(font=("Arial", 15))
    ECG = Entry(ECGFrame)
    ECG.grid(row=2, column=2, sticky='nw')


    thalachFrame = LabelFrame(mainWindow, text="thalach(71-202)")
    thalachFrame.grid(row=4, column=1)
    thalachFrame.config(font=("Arial", 15))
    thalach = Entry(thalachFrame)
    thalach.grid(row=2, column=2, sticky='nw')

    exangFrame = LabelFrame(mainWindow, text="exAngina(0/1)")
    exangFrame.grid(row=4, column=2)
    exangFrame.config(font=("Arial", 15))
    exang = Entry(exangFrame)
    exang.grid(row=2, column=2, sticky='nw')


    oldpeakFrame = LabelFrame(mainWindow, text="Old Peak(0-6.2)")
    oldpeakFrame.grid(row=5, column=0)
    oldpeakFrame.config(font=("Arial", 15))
    oldpeak = Entry(oldpeakFrame)
    oldpeak.grid(row=2, column=2, sticky='nw')

    slopeFrame = LabelFrame(mainWindow, text="Slope(0,1,2)")
    slopeFrame.grid(row=5, column=1)
    slopeFrame.config(font=("Arial", 15))
    slope = Entry(slopeFrame)
    slope.grid(row=2, column=2, sticky='nw')

    caFrame = LabelFrame(mainWindow, text=" C. A (0-3)")
    caFrame.grid(row=5, column=2)
    caFrame.config(font=("Arial", 15))
    ca = Entry(caFrame)
    ca.grid(row=2, column=2, sticky='nw')


    thalFrame = LabelFrame(mainWindow, text=" THAL(0,1,2,3)")
    thalFrame.grid(row=6, column=1)
    thalFrame.config(font=("Arial", 15))
    thal = Entry(thalFrame)
    thal.grid(row=2, column=2, sticky='nw')


    analyseButton = Button(mainWindow, text="..................ANALYZE/ PREDICT.....................", font=('Arial', 15), bg = 'blue', command=takeInput)
    analyseButton.grid(row=8, column=0, columnspan=10)



    return
