import pymysql


def insertion(name,sex,age,rollno,sublist,adr,em,phno,lang):
    cur.execute("insert into form values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,sex,age,rollno,sublist,adr,em,phno,lang))
    #cur.execute("insert into form values('"+name+"','"+sex+"','"+age+"','"+rollno+"','"+sublist+"','"+adr+"','"+em+"','"+phno+"','"+lang+"')")
    con.commit()

def display():
    cur.execute("select * from form")
    result=cur.fetchall()
    return result

def check(rno,em,ph):
    cur.execute("select * from form where rno=%s or email=%s or phone_number=%s",(rno,em,ph))
    temp=cur.rowcount
    return(temp)
    
        
    
    
#start
con=pymysql.connect(host="localhost",user="root",password="boot")
cur=con.cursor()

cur.execute("create database if not exists tki")
cur.execute("use tki")
#cur.execute("drop table if exists form")
cur.execute("create table if not exists form (name varchar(30) not null,sex varchar(6),"+\
            "age int,rno int primary key,subjects varchar(100),"+\
            "address varchar(100),email varchar(50) unique,phone_number char(10) unique,"+\
            "language varchar(20))")




