from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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

        self.bg=ImageTk.PhotoImage(file="C:\\Users\\Prathamesh\\Desktop\\attend me\\images\\bg2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file="C:\\Users\\Prathamesh\\Desktop\\attend me\\images\\bg2.jpg")
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

        img=Image.open("C:\\Users\\Prathamesh\\Desktop\\attend me\\images\\bg2.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=440,width=200)

        img1=Image.open("C:\\Users\\Prathamesh\\Desktop\\attend me\\images\\bg2.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
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



        
        

        





if __name__== "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
