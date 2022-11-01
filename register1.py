from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
#import mysql.connector

class register:
     def __init__(self,root):
        self.root=root
        self.root.title("RAILWAY REGISTER")
        self.root.geometry("1600x900+0+0")

        #................REGISTER FUNCTION VARIABLES.....................
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_contact=StringVar()
        self.var_mail=StringVar()
        self.var_que=StringVar()
        self.var_ans=StringVar()
        self.var_passwd=StringVar()
        self.var_pw1=StringVar()
        self.var_check=IntVar()

        #........BACKGROUND IMAGE..............
        self.bg=ImageTk.PhotoImage(file=r"rail.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        #...........REGISTER PAGE............
        frame=Frame(self.root,bg="white")
        frame.place(x=380,y=100,width=800,height=550)
        #.............REGISTER ICON.........
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=280,y=20)
        #......LABEL AND ENTRY.........
        fname=Label(frame,text="FIRST NAME:",font=("times new roman",12,"bold"),bg="white")
        fname.place(x=50,y=100)
        self.txtname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",11,"bold"))
        self.txtname.place(x=50,y=130,width=250)

        Lname=Label(frame,text="LAST NAME:",font=("times new roman",12,"bold"),bg="white")
        Lname.place(x=450,y=100)
        self.txtname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",11,"bold"))
        self.txtname.place(x=450,y=130,width=250)

        gender=Label(frame,text="GENDER:",font=("times new roman",12,"bold"),bg="white")
        gender.place(x=50,y=160)
        #.....SELECT COMBO BOX.......
        self.combo_gender=ttk.Combobox(frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),state="readonly")
        self.combo_gender["values"]=("SELECT","MALE","FEMALE","OTHER")
        self.combo_gender.place(x=50,y=190,width=250)
        self.combo_gender.current(0)

        DOB=Label(frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        DOB.place(x=450,y=160)
        self.txtno=ttk.Entry(frame,textvariable=self.var_DOB,font=("times new roman",11,"bold"))
        self.txtno.place(x=450,y=190,width=250)

        

        contact=Label(frame,text="CONTACT NO.:",font=("times new roman",12,"bold"),bg="white")
        contact.place(x=50,y=220)
        self.txtno=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",11,"bold"))
        self.txtno.place(x=50,y=250,width=250)

        mail=Label(frame,text="EMAIL:",font=("times new roman",12,"bold"),bg="white")
        mail.place(x=450,y=220)
        self.txtmail=ttk.Entry(frame,textvariable=self.var_mail,font=("times new roman",11,"bold"))
        self.txtmail.place(x=450,y=250,width=250)

        que=Label(frame,text="SELECT SECURITY QUESTION:",font=("times new roman",12,"bold"),bg="white")
        que.place(x=50,y=280)
        #.....SELECT COMBO BOX.......
        self.combo_que=ttk.Combobox(frame,textvariable=self.var_que,font=("times new roman",11,"bold"),state="readonly")
        self.combo_que["values"]=("SELECT","YOUR BIRTH PLACE","YOUR PET NAME","YOUR FAV. PLACE")
        self.combo_que.place(x=50,y=310,width=250)
        self.combo_que.current(0)

        ans=Label(frame,text="SECURITY ANSWER:",font=("times new roman",12,"bold"),bg="white")
        ans.place(x=450,y=280)
        self.txtans=ttk.Entry(frame,textvariable=self.var_ans,font=("times new roman",11,"bold"))
        self.txtans.place(x=450,y=310,width=250)

        passwd=Label(frame,text="PASSWORD:",font=("times new roman",12,"bold"),bg="white")
        passwd.place(x=50,y=340)
        self.txtpw=ttk.Entry(frame,textvariable=self.var_passwd,font=("times new roman",11,"bold"))
        self.txtpw.place(x=50,y=370,width=250)

        pw1=Label(frame,text="CONFIRM PASSWORD:",font=("times new roman",12,"bold"),bg="white")
        pw1.place(x=450,y=340)
        self.txtp=ttk.Entry(frame,textvariable=self.var_pw1,font=("times new roman",11,"bold"))
        self.txtp.place(x=450,y=370,width=250)

        #......................CHECK BUTTON................
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions.",font=("times new roman",11,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=400)


        #........................BUTTON.............
        img=Image.open(r"register.png")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roamn",15,"bold") )
        b1.place(x=50,y=450,width=200)

        img1=Image.open(r"login.png")
        img1=img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage2,borderwidth=0,cursor="hand2",font=("times new roamn",15,"bold") )
        b2.place(x=450,y=450,width=200)

     #............FUNCTION ................
     def register_data(self):
          if self.var_fname.get()=="" or self.var_mail.get()=="" or self.var_lname.get()=="" or self.var_gender.get()=="SELECT" or self.var_DOB.get()=="" or self.var_contact.get()=="" or self.var_que.get()=="SELECT" or self.var_ans.get()==""or self.var_passwd.get()=="" or self.var_pw1.get()=="":
               messagebox.showerror("ERROR","ALL FIELDS ARE REQUIERD")
          elif self.var_passwd.get()!=self.var_pw1.get():
               messagebox.showerror("ERROR","PASSWORD AND CONFIRM PASSWORD MUST BE SAME")
          elif self.var_check.get()==0:
               messagebox.showerror("ERROR","PLEASE AGREE OUR TERMS AND CONDITIONS")
          
                              



      
    
if __name__=="__main__":
    root=Tk()
    app=register(root)
    root.mainloop()
    
