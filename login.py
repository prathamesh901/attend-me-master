from re import M
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        self.bg=ImageTk.PhotoImage(file="C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=500)

        img1=Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\login.jpeg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username_lbl=Label(frame,text="Enter Gmail",font=("times new roman",20,"bold"),fg="white",bg="black")
        username_lbl.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",17,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        password_lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password_lbl.place(x=40,y=245)


        self.txtpass=ttk.Entry(frame,font=("times new roman",17,"bold"))
        self.txtpass.place(x=40,y=280,width=270)
        self.txtpass.config(show="*")

        # img2=Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        # img2=img2.resize((25,25),Image.ANTIALIAS)
        # self.photoimage2=ImageTk.PhotoImage(img2)
        # lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        # lblimg1.place(x=650,y=333,width=25,height=25)

        # img3=Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        # img3=img3.resize((25,25),Image.ANTIALIAS)
        # self.photoimage3=ImageTk.PhotoImage(img3)
        # lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        # lblimg1.place(x=650,y=423,width=25,height=25)

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",18,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=330,width=120,height=43)

        registerbtn=Button(frame,text="Create New Account",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=385,width=160)

        forgetbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=12,y=410,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All feilds are required")
        elif self.txtuser.get()=="prathamesh" and self.txtpass.get()=="Bvit@2002":
             messagebox.showinfo("Success","Welcome")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bvit@2002",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                     self.txtuser.get(),
                                                                                     self.txtpass.get()
                                                                         ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("yesno","Acess Only Authority Person")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security quetion",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bvit@2002",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityq=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                qury=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(qury,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()


    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bvit@2002",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x500+610+170")
                

                l=Label(self.root2,text="Forget Password",font=("times new roman",18,"bold"),fg="darkred",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_q=Label(self.root2,text="Select Security Quetions",font=("times new roman",15,"bold"),fg="black")
                security_q.place(x=50,y=80)

                self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_q["values"]=("Select","Select Your Birth Place","Your Bestfriend Name","Your Pet Name")
                self.combo_security_q.place(x=50,y=110,width=250)
                self.combo_security_q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="darkgreen",fg="white")
                btn.place(x=130,y=350)



                

class Register:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=StringVar()

        self.bg=ImageTk.PhotoImage(file="C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file="C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        left_bg=Label(self.root,image=self.bg1)
        left_bg.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,))
        self.txt_email.place(x=370,y=200,width=250)
            

        security_q=Label(frame,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Select Your Birth Place","Your Bestfriend Name","Your Pet Name")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        paswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        paswd.place(x=50,y=310)

        self.txt_paswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_paswd.place(x=50,y=340,width=250)


        confirm_pass=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pass.place(x=370,y=310)

        self.txt_confirm_pass=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pass.place(x=370,y=340,width=250)

        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms And Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        img=Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\register.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=440,width=200)

        img1=Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\cancel1.webp")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=440,width=200)

    def register_data(self): 
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="":
            messagebox.showerror("Error","All feilds are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passwoed and Conform password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Bvit@2002",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error,User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityq.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()

    
        


        



if __name__== "__main__":
    main()