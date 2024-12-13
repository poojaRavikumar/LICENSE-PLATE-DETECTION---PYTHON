# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:19:05 2020

@author: Admin
"""
from tkinter import *
import os
import mysql.connector
import Main
def Signup(): 
    global pwordE
    global nameE
    global roots
 
    roots = Tk()
    roots.title('Login')
    intruction = Label(roots, text='Please Enter your Credidentials\n') 
    intruction.grid(row=0, column=0, sticky=E) 
 
    nameL = Label(roots, text='Username: ') 
    pwordL = Label(roots, text='Password: ') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W)
 
    nameE = Entry(roots) 
    pwordE = Entry(roots, show='*') 
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1) 
 
    signupButton = Button(roots, text='login', command=login_verify)
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop() 
def login_verify():
    username1 = nameE.get()
    password1 = pwordE.get()
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database = "loginDB")
    cur = myconn.cursor()
    try:
        roots.destroy()
        sql="select * from login"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
                    name = row[0]
                    pwd = row[1]
                    if name == username1 and pwd == password1:
                        print("yaass")
                        getImageName();
                        #Main.main()
        Signup()
    except:  
        myconn.rollback()
def getImageName():
    global imagename
    root1 = Tk()
    root1.title('Load image')
    intruction = Label(root1, text='enter the image name to load\n') 
    intruction.grid(row=0, column=0, sticky=E) 
 
    nameL = Label(root1, text='Imagename: ') 
    nameL.grid(row=1, column=0, sticky=W) 

 
    imagename = Entry(root1)  
    imagename.grid(row=1, column=1)
 
    signupButton = Button(root1, text='load', command=pass_param)
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()
def pass_param():
    imagename1 = imagename.get()
    Main.main(imagename1)
Signup()