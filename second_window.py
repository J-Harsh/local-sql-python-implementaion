from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk


top=Tk()
top.geometry("1000x1000")

def end():
    top.destroy()
    
def disp():
    import sql_tki
    result=sql_tki.display()
    print(result)
    rowcn=len(result)
    colcn=len(result[0])
    #another top level
    last=Toplevel(top)
    last.title("Your data")
    
    e1=Entry(last,width=20, fg='red')
    e1.insert(END,"Name")
    e2=Entry(last,width=20, fg='red')
    e2.insert(END,"Gender")
    e3=Entry(last,width=20, fg='red')
    e3.insert(END,"Age")
    e4=Entry(last,width=20, fg='red')
    e4.insert(END,"UID")
    e5=Entry(last,width=20, fg='red')
    e5.insert(END,"Subjects")
    e6=Entry(last,width=20, fg='red')
    e6.insert(END,"Address")
    e7=Entry(last,width=20, fg='red')
    e7.insert(END,"Email")
    e8=Entry(last,width=20, fg='red')
    e8.insert(END,"Contact")
    e9=Entry(last,width=20, fg='red')
    e9.insert(END,"Languages")
    e1.grid(row=0,column=0)
    e2.grid(row=0,column=1)
    e3.grid(row=0,column=2)
    e4.grid(row=0,column=3)
    e5.grid(row=0,column=4)
    e6.grid(row=0,column=5)
    e7.grid(row=0,column=6)
    e8.grid(row=0,column=7)
    e9.grid(row=0,column=8)

    for i in range(rowcn):
        for j in range(colcn):
            e=Entry(last,width=20,fg='red')
            e.grid(row=i+1,column=j)
            e.insert(END,result[i][j])

    bye=Button(last,text="Click here to exit",command=end)
    bye.grid(row=i+2,column=0)
    
    last.mainloop()

    
    

#title
top.title("Form has been submitted")

#Label 1
lb1=Message(top,text="Your form has been submitted successfully\nDo the either of the following steps to contiune:",width=500,relief=RAISED)
lb1.place(x=350,y=250)

#button1
im1=Image.open("E:\\Computer\\python tution\\python tution\\tkinter project+mysql\images\\exit.png")
im1=im1.resize((50,30))
filename1=ImageTk.PhotoImage(im1)
but1=Button(top,image=filename1,command=end)
but1.place(x=300,y=300)

#button2
im2=Image.open("E:\\Computer\\python tution\\python tution\\tkinter project+mysql\images\\print.png")
im2=im2.resize((50,30))
filename2=ImageTk.PhotoImage(im2)
but2=Button(top,image=filename2,command=disp)
but2.place(x=600,y=300)

top.mainloop()
