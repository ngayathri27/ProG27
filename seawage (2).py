import pandas as pd #for reading dataset
import numpy as np # array handling functions
from time import sleep

import smtplib
from email.message import EmailMessage
import imghdr
from time import sleep
email_add = 'ngayathri278@gmail.com'
email_pass = "ykveujjpjyeouinq"
msg = EmailMessage()
msg['Subject'] = "sewage monitoring"
msg['From'] = "ngayathri278@gmail.com"
msg['To'] = "skeerthana0904@gmail.com"
msg.set_content("Block is there. Contact your local authority")

def email(): 
    with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
        smtp.login(email_add,email_pass)
        smtp.send_message(msg)

##email()
dataset = pd.read_csv("DATA.csv")#reading datasetn
x = dataset.iloc[:,:-1].values #locating inputs
y = dataset.iloc[:,-1].values #locating outputs

from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y= labelencoder_y.fit_transform(y)



#printing X and Y
print("x=",x)
print("y=",y)

from sklearn.model_selection import train_test_split # for splitting dataset
x_train,x_test,y_train,y_test = train_test_split(x ,y, test_size = 0.25 ,random_state = 0)
#printing the spliited dataset
print("x_train=",x_train)
print("x_test=",x_test)
print("y_train=",y_train)
print("y_test=",y_test)
 #importing algorithm
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
classifier.fit(x_train,y_train)#trainig Algorithm

y_pred=classifier.predict(x_test) #testing model
print("y_pred",y_pred) # predicted output
try:
    import serial
    ser = serial.Serial('COM3',baudrate=9600,timeout=0.3)
    ser.flushInput()
    A=1
    B=1
    while True:
        a=ser.readline().decode('ascii') # reading serial data
        print(a)
        b=a
        for letter in b:
            if(letter =='K'):
                D1 =b[4]+b[5]
                print("WATER LEVEL SENSOR VALUE : ",D1)
                a1 =int(D1)

            if(letter =='F'):
                D2 =b[7]+b[8]
                print("FLOW SENSOR : ",D2)
                a2 =int(D2)
            if(letter =='R'):
                D3 =b[10]
                print(" RAIN SENSOR: ",D3)
                a3 =int(D3)
##            if(letter == 'G'):
##                D3 = b[9]
##                print(" GAS SENSOR: ",D3)
##                a4 = int(D3)     



                ##PREDICTED OUTPUT
                OUTPUT = classifier.predict([[a1,a2,a3]])
                print('DECISION TREE OUTPUT: ',OUTPUT)
                                
                
            if(OUTPUT ==1):
               ser.write('1'.encode())
               email()
               print("block")
##                





except Exception as e:
    print(e)
          
          
            

            
