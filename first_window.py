from tkinter import *
from tkinter import messagebox
import os
import time


#variables
i=5

#functions,some are done by using register function because of entries and text,
def mb():
    filewin=Toplevel(top)
    label=Label(filewin,text='Command Executed',relief=FLAT)
    label.pack()


def chk(temp):
    temp=temp.get()
    if(temp=="" or temp.isdigit()==True):
        chkerror=Label(top,text="Invalid entry detected,kindly re-check",relief=RAISED)
        chkerror.place(x=900,y=add+450)
        return ""
    else:
        return temp

def chkrno(temp):
    temp=temp.get()
    if(temp=="" or temp.isalpha()==True):
        chkerror=Label(top,text="Invalid Roll number,kindly re-check",relief=RAISED)
        chkerror.place(x=900,y=add+450)
        return ""
    else:
        return temp
    
def chkph(temp):
    temp=temp.get()
    if(temp=="" or temp.isalpha()==True or len(temp)!=10):
        chkerror=Label(top,text="Invalid phone number,kindly re-check",relief=RAISED)
        chkerror.place(x=900,y=add+450)
        return ""
    else:
        return temp

def chkem(temp):
    temp=temp.get()
    print(temp)
    if( ("@" in temp) and (".com" in temp)):
        return temp
    else:
        chkerror=Label(top,text="Invalid email,kindly re-check",relief=RAISED)
        chkerror.place(x=900,y=add+450)
        return ""
    
def but():
    global timer_text
    global timer
    temp=slb.curselection()

    if(chk(e1)!="" and radioVar.get()!=0 and scaleVar.get()!=0 and chkrno(e2)!="" and len(temp)!=0 and adtb.get()!="" and chkph(e3)!=""and (lang1.get()!=0 or lang2.get()!=0) and radioVartc.get()!=0 and chkem(e4)):
        
        #name
        name=e1.get()
        #sex
        if(radioVar.get()==1):
            sex="Male"
        elif(radioVar.get()==2):
            sex="Female"
        else:
            sex="Other"
        #age
        age=scaleVar.get()
        #rno
        rno=e2.get()
        #subject list
        sublist=["Physics","Chemistry","Maths","Computer Science","Physcial Studies"]
        s=""
        for i in temp:
            s=s+sublist[i]+","
        s=s[:len(s)-1]
        print(s)
        #address
        address=adtb.get()
        #email address
        email=e4.get()
        #phone number
        phno=e3.get()
        #language
        if(lang1.get()==1 and lang2.get()==1):
            lang="English,Hindi"
        elif(lang1.get()==1):
            lang="English"
        else:
            lang="Hindi"

        import sql_tki
        if(sql_tki.check(rno,email,phno)==0):
            sql_tki.insertion(name,sex,age,rno,s,address,email,phno,lang)
            success=Message(top,text="Form Submitted successfully")
            success.place(x=900,y=add+480)
            top.destroy()
            import second_window
            
            
        else:
            msg=messagebox.showinfo("Error","Either roll number,email or phone number already exists")
            timer=Label(top,textvar=timer_text,relief=RAISED)
            timer.place(x=900,y=add+510)
            restart()
        
        
        
    else:
        sub.configure(state=DISABLED)
        error=Label(top,text="Error: No entries can be left unfilled",relief=RAISED)
        error.place(x=900,y=add+480)
        timer=Label(top,textvar=timer_text,relief=RAISED)
        timer.place(x=900,y=add+510)
        restart()


def restart():
    global i
    global timer_text
    timer_text.set("Re-fill the form in "+str(i)+" seconds")
    i=i-1
    timer.after(600,restart)
    if(i==-1):
        top.destroy()
        os.startfile("first_window.py")
    
              
top=Tk()
top.geometry('5000x5000')
timer_text=StringVar()

#title
top.title("Trial Form")

#menubar
menubar=Menu(top)

fm = Menu(menubar, tearoff=0)
fm.add_command(label="New",command=mb)
fm.add_command(label = "Open",command=mb)
fm.add_command(label = "Save",command=mb)
fm.add_command(label = "Save as",command=mb)
fm.add_command(label = "Close",command=mb)
fm.add_separator()
fm.add_command(labe='Exit',command=top.quit)
menubar.add_cascade(label='File',menu=fm)

em = Menu(menubar, tearoff = 0)
em.add_command(label="Cut",command=mb)
em.add_command(label="Copy",command=mb)
em.add_command(label="Paste",command=mb)
em.add_command(label="Delete",command=mb)
em.add_command(label="Select",command=mb)
em.add_command(label="Select all",command=mb)
menubar.add_cascade(label="Edit",menu=em)

top.config(menu=menubar)

add=40
#Label                              <This is a tuple where,first is font name followed by size and style(inner bracket only)>
head=Label(top,text="Trial form",font=("Times New Roman",25,'underline'),relief=FLAT,fg="Blue",bg="Cyan") #important
head.place(x=680,y=5)

#Entry 1
el1=Label(top,text="Enter your name:",relief=FLAT)
el1.place(x=600,y=add+20)
e1=Entry(top,bd=1)
e1.place(x=720,y=add+20)

#Entry 2
el2=Label(top,text="Enter your Gender:",relief=FLAT)
el2.place(x=600,y=add+50)
radioVar=IntVar()
r1=Radiobutton(top,text='Male',variable=radioVar,value=1)
r2=Radiobutton(top,text='Female',variable=radioVar,value=2)
r3=Radiobutton(top,text='Other',variable=radioVar,value=3)
r1.place(x=720,y=add+50)
r2.place(x=780,y=add+50)
r3.place(x=850,y=add+50)

#Entry 3
el3=Label(top,text="Enter your Age:",relief=FLAT)
el3.place(x=600,y=add+90)
scaleVar=DoubleVar()
scale=Scale(top,variable=scaleVar,orient=HORIZONTAL,from_=0,to=80,length=200)
scale.place(x=720,y=add+70)

#Entry 4
el4=Message(top,text="Enter your\nRoll Number:",relief=FLAT,width=100)
el4.place(x=597,y=add+120)
e2=Entry(top,bd=1)
e2.place(x=720,y=add+130)

#Entry 5
el5=Label(top,text="Select your subjects:",relief=FLAT)
el5.place(x=600,y=add+170)
slb=Listbox(top,selectmode=MULTIPLE,height=5)
slb.insert(1,"Physics")
slb.insert(2,"Chemistry")
slb.insert(3,"Maths")
slb.insert(4,"Computer Science")
slb.insert(5,"Physical Studies")
slb.place(x=720,y=add+172)

#Entry 6
el6=Label(top,text="Enter your address:",relief=FLAT)
el6.place(x=600,y=add+270)
adtb=Entry(top,bd=1,width=40)
adtb.place(x=720,y=add+270)

#Entry 7
el7=Message(top,text="Enter your phone number:",relief=FLAT,width=100)
el7.place(x=600,y=add+340)
e3=Entry(top,bd=1)
e3.place(x=720,y=add+340)

#Entry 8
el8=Message(top,text="Select your desired\nlanguage:",width=100)
el8.place(x=600,y=add+390)
lang1=IntVar()
lang2=IntVar()
lang1bt=Checkbutton(top,text="English",variable=lang1,onvalue=1,offvalue=0)
lang2bt=Checkbutton(top,text="Hindi",variable=lang2,onvalue=1,offvalue=0)
lang1bt.place(x=720,y=add+390)
lang2bt.place(x=780,y=add+390)

#Entry 9
el9=Message(top,text="Terms and\nConditions:",width=100)
el9.place(x=600,y=add+440)
radioVartc=IntVar()
toc1=Radiobutton(top,text='Yes',variable=radioVartc,value=1)
toc2=Radiobutton(top,text='No',variable=radioVartc,value=2)
toc1.place(x=720,y=add+440)
toc2.place(x=780,y=add+440)

#Entry 10
el10=Message(top,text="Enter your email address:",width=100)
el10.place(x=600,y=add+300)
e4=Entry(top,bd=1)
e4.place(x=720,y=add+300)

#Submit button
sub=Button(top,text="Submit",fg="Black",bg="White",activebackground="Black",activeforeground="White",command=but)
sub.place(x=720,y=add+480)

top.mainloop()









