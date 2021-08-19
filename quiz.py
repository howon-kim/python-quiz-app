import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time
import csv
import os
from datetime import datetime
from quizFile import *


def signUpPage():
    root.destroy()
    global sup
    global wr
    sup = Tk()
    
    fname = StringVar()
    lname = StringVar()
    age = StringVar()
    wr = None
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="blue")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="정보입력",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="이름",fg='black',bg='white')
    flabel.place(relx=0.21,rely=0.4)
    fentry = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fentry.config(width=42)
    fentry.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="성",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = lname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="나이",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='black', textvariable = age)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)


    
    def addUserToDataBase():
        global wr
        fname = fentry.get()
        lname = user.get()
        age = pas.get()

        filename = os.path.join(str(fentry.get()) + "_" + str(user.get()) + "_" + str(pas.get()) + ".csv")
        f = open(filename, 'a', encoding='utf-8-sig')
        wr = csv.writer(f)

        wr.writerow([fname, lname, age, datetime.now()])

        
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FIRSTNAME text, LASTNAME text, AGE text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?)",(fname,lname,age)) 
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        print(z)
        conn.close()
        #loginPage(z)
        sup.destroy()

        menu()

    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="white",fg='blue')
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()

def menu():
    global menu 
    menu = Tk()
    
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="blue")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text='리뷰미 웹소설 문제',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    
    level = Label(menu_frame,text='웹소설 종류를 선택해 주세요',bg="white",font="calibri 18")
    level.place(relx=0.25,rely=0.3)
    
    
    var = IntVar()
    easyR = Radiobutton(menu_frame,text='아카데미 고인물',bg="white",font="calibri 16",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.4)
    
    mediumR = Radiobutton(menu_frame,text='피자 타이거 스파게티 드래곤',bg="white",font="calibri 16",value=2,variable = var)
    mediumR.place(relx=0.25,rely=0.5)
    
    hardR = Radiobutton(menu_frame,text='하렘의 남자들',bg="white",font="calibri 16",value=3,variable = var)
    hardR.place(relx=0.25,rely=0.6)
    
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            wr.writerow([easyR.cget("text")])
            menu.destroy()
            easy()

        elif x == 2:
            wr.writerow([easyR.cget("text")])
            menu.destroy()
            medium()
        
        elif x == 3:
            wr.writerow([easyR.cget("text")])
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()

def easy():
    global easy
    easy = Tk()
    
    easy_canvas = Canvas(easy,width=720,height=440,bg="#101357")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="white")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)


    
    
    def countDown():
        check = 0
        for k in range(30, 0, -1):
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0

    global score
    score = 0
        
    li = ['',0,1,2,3,4,5,6,7,8,9]
    x = random.choice(li[1:])

    ques = Label(easy_frame,text =quiz_academy[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_frame,text=quiz_academy[x][1],font="calibri 10",value=quiz_academy[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=quiz_academy[x][2],font="calibri 10",value=quiz_academy[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=quiz_academy[x][3],font="calibri 10",value=quiz_academy[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=quiz_academy[x][4],font="calibri 10",value=quiz_academy[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 

    e = Radiobutton(easy_frame,text=quiz_academy[x][5],font="calibri 10",value=quiz_academy[x][5],variable = var,bg="white")
    e.place(relx=0.5,rely=0.82,anchor=CENTER) 

    f = Radiobutton(easy_frame,text=quiz_academy[x][6],font="calibri 10",value=quiz_academy[x][6],variable = var,bg="white")
    f.place(relx=0.5,rely=0.92,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(easy)
    timer.place(relx=0.8,rely=0.2,anchor=CENTER)
        
    
    def display():
        nextQuestion.configure(text='다음문제',command=calc)

        if len(li) == 1:
                easy.destroy()
                showMark(score)
                #f.close()
        if len(li) == 2:
            nextQuestion.configure(text='끝내기',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =quiz_academy[x][0])
            
            a.configure(text=quiz_academy[x][1],value=quiz_academy[x][1])
      
            b.configure(text=quiz_academy[x][2],value=quiz_academy[x][2])
      
            c.configure(text=quiz_academy[x][3],value=quiz_academy[x][3])
      
            d.configure(text=quiz_academy[x][4],value=quiz_academy[x][4])

            e.configure(text=quiz_academy[x][5],value=quiz_academy[x][5])

            f.configure(text=quiz_academy[x][6],value=quiz_academy[x][6])

            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        temp = []
        temp.append(abs(len(li) - 11))
        print(var.get())
        if (var.get() in sol_academy):
            score+=1
            temp.append("o")
        else:
            temp.append("x")
        temp.append(str(30 - int(timer.cget("text"))))
        print(temp)
        wr.writerow(temp)
        display()
    
    nextQuestion = Button(easy_frame,command=calc,text="다음문제")
    nextQuestion.place(relx=0.87,rely=0.92,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    easy.mainloop()
    

def showMark(mark):
    global sh
    sh = Tk()

    def exit():
        sh.destroy()



    
    show_canvas = Canvas(sh,width=720,height=440,bg="#101357")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = "Your score is "+str(mark)
    mlabel = Label(show_canvas,text=st,fg="black")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)

    sp = Button(show_canvas,text='종료',padx=5,pady=5,width=5,command = exit,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    sh.mainloop()


def start():
    global root 
    root = Tk()
    canvas = Canvas(root,width = 720,height = 440)
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="back.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='시작',command = signUpPage) 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()
