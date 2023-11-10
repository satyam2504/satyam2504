from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main_project import FaceRecognitionSystem


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN WITH SMART ATTENDANCE MANAGEMENT SYSTEM")
        self.root.geometry("2256x1504+0+0")
        self.root.wm_iconbitmap("face.ico")

        # self.bg=ImageTk.PhotoImage(file="images/SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        img1 = Image.open("college_images/5.jpg")
        img1 = img1.resize((1500,1504), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoImg1)
        bg_lbl.place(x=0,y=0,width=1500,height=1504)

        title=Label(bg_lbl,text="ADMIN LOGIN",font=("arial",20,"bold"),bg="red",fg="black")
        title.place(x=0.9,y=195,width=330,height=30)

         # ==================== Project buttom(description) ==================================================
        # downtitle=Label(self.root,text="Note:Enter valid username and valid password",font=("arial",20,"bold"),bd=2,relief=RAISED,bg="yellow",fg="blue")
        # downtitle.place(x=0,y=740,width=1600,height=35)

        # myname=Label(self.root,text="Developed Raj",fg="yellow",bg="yellow",font=("arial",18,"bold"))
        # myname.place(x=0,y=0)
        
        # img10 = Image.open("college_images/ssm.jpg")
        # img10 = img10.resize((1270,80), Image.ANTIALIAS)
        # self.photoImg10 = ImageTk.PhotoImage(img10)
        # bg_lbl1=Label(bg_lbl,image=self.photoImg10)
        # bg_lbl1.place(x=0,y=0,width=1270,height=80)

        # img11 = Image.open("college_images/facialrecognition.png")
        # img11 = img11.resize((500,120), Image.ANTIALIAS)
        # self.photoImg11 = ImageTk.PhotoImage(img11)
        # bg_lbl22=Label(bg_lbl,image=self.photoImg11)
        # bg_lbl22.place(x=500,y=0,width=500,height=120)

        # img13 = Image.open("college_images/smart-attendance.jpg")
        # img13 = img13.resize((550,120), Image.ANTIALIAS)
        # self.photoImg13= ImageTk.PhotoImage(img13)
        # bg_lbl12=Label(bg_lbl,image=self.photoImg13)
        # bg_lbl12.place(x=1000,y=0,width=550,height=120)


        frame=Frame(self.root,bg="yellow")
        frame.place(x=5,y=230,width=330,height=400)

        img1=Image.open("college_images/LoginIconAppl.png")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="yellow",borderwidth=0)
        lblimg1.place(x=122,y=230,width=90,height=90)

        get_str=Label(frame,text="Get Started",font=("arial",20,"bold"),fg="black",bg="yellow")
        get_str.place(x=90,y=88)

        # label
        username=lbl=Label(frame,text="Username",font=("arial",12,"bold"),fg="black",bg="yellow")
        username.place(x=70,y=125)


        self.txtuser=StringVar()
        self.txtpass=StringVar()

        txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("arial",15,"bold"))
        txtuser.place(x=40,y=150,width=270)

        password=lbl=Label(frame,text="Password",font=("arial",12,"bold"),fg="black",bg="yellow")
        password.place(x=70,y=195)

        txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("arial",15,"bold"),show="*")
        txtpass.place(x=40,y=220,width=270)

        # ======Icon Images=================
        img2=Image.open("college_images/LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="yellow",borderwidth=0)
        lblimg1.place(x=10,y=380,width=25,height=25)


        img3=Image.open("college_images/lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="yellow",borderwidth=0)
        lblimg1.place(x=10,y=452,width=25,height=25)

        # LoginButton
        btn_login=Button(frame,text="Login",borderwidth=3,relief=RAISED,command=self.login,cursor="hand2",font=("arial",16,"bold"),fg="yellow",bg="red" ,activebackground="#B00857")
        btn_login.place(x=110,y=270,width=120,height=35)
        # registerbutton
        registerbtn=Button(frame,text="NEW REGISTRATION",command=self.rigister_window,font=("arial",10,"bold"),fg="red",bg="yellow",activeforeground="yellow",activebackground="yellow")
        registerbtn.place(x=85,y=320,width=180)

        # forgetpassbtn
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("arial",10,"bold"),borderwidth=2,fg="black",bg="yellow",activeforeground="yellow",activebackground="yellow")
        registerbtn.place(x=80,y=355,width=160)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required",parent=self.root)
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to smart attendence system",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="facial_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            ))

            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Inavalid Username & password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only Authority Person",parent=self.root)
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=FaceRecognitionSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")

    # =====================reset password=======================================
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select" or self.txt_security.get()=="" or self.txt_newpass=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="facial_recognition")
                cur=conn.cursor()
                query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                # print(row)
                if row==None:
                    messagebox.showerror("Error","Please select the correct security quetion/Enter answer",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    cur.execute(query,value)
                    # row2=cur.fetchone()
                    conn.commit() 
                    conn.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                    self.root2.destroy()
                    # self.reset()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due To:{str(es)}",parent=self.root2)
        
        
    # =============================================forgrt password window=============================      
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Plaese Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="facial_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Plaese enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+200")
                self.root2.configure(bg="yellow")

                l=Label(self.root2,text="Forget Password",font=("arial",20,"bold"),fg="red",bg="yellow")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Quetions",font=("arial",15,"bold"),bg="yellow",fg="yellow")
                security_Q.place(x=50,y=80)

                self.combo_securiy_Q=ttk.Combobox(self.root2,font=("arial",15,"bold"),state="readonly")
                self.combo_securiy_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_securiy_Q.place(x=50,y=110,width=250)
                self.combo_securiy_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("arial",15,"bold"),bg="yellow",fg="yellow")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("arial",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("arial",15,"bold"),bg="yellow",fg="yellow")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("arial",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("arial",15,"bold"),fg="White",bg="green")
                btn.place(x=120,y=290,width=100)
 


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ==================varibles====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        

        # ============bg image==================
        # self.bg=ImageTk.PhotoImage(file="college_images/h.jpg")
        # bg_lbl=Label(self.root,image=self.bg)
        # bg_lbl.place(x=0,y=0,width=1530,height=800)

        
        # ============left image==================
        self.bg1=ImageTk.PhotoImage(file="college_images/coll.jpg")
        # bg1 = bg1.resize((400,450), Image.ANTIALIAS)
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=0,y=0,width=600,height=750)

        # ==============main Frame=====================
        frame=Frame(self.root,bg="yellow")
        frame.place(x=630,y=110,width=640,height=490)

        register_lbl=Label(frame,text="REGISTER HERE:-",font=("arial",30,"bold"),fg="black",bg="yellow")
        register_lbl.place(x=20,y=20)

        # ==============label and entry===========================

        # ------------------row1
        fname=Label(frame,text="First Name",font=("arial",15,"bold"),bg="yellow",fg="black")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("arial",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("arial",15,"bold"),bg="yellow",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("arial",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        # -----------------row2

        contact=Label(frame,text="Contact No",font=("arial",15,"bold"),bg="yellow",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("arial",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("arial",15,"bold"),bg="yellow",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("arial",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        # ------------------row3

        security_Q=Label(frame,text="Select Security Quetions",font=("arial",15,"bold"),bg="yellow",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_securiy_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("arial",15,"bold"),state="readonly")
        self.combo_securiy_Q["values"]=("Select","Birth Place","Nick Name","Pet Name")
        self.combo_securiy_Q.place(x=50,y=270,width=250)
        self.combo_securiy_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("arial",15,"bold"),bg="yellow",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("arial",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        # ----------------------row4

        pswd=Label(frame,text="Password ",font=("arial",15,"bold"),bg="yellow",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("arial",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("arial",15,"bold"),bg="yellow",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("arial",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # ===================checkbutton=================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",bg='blue',font=("arial",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        # =================buttons========================
        # img=Image.open("college_images/register-now-button1.jpg")
        # img=img.resize((200,55),Image.ANTIALIAS)
        # self.photoimage=ImageTk.PhotoImage(img)
        # b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("arial",15,"bold"),fg="yellow")
        # b1.place(x=10,y=420,width=200)
        b1=Button(frame,text="Register Now",command=self.register_data,borderwidth=0,cursor="hand2",font=("arial",15,"bold"),bg='blue',fg='yellow')
        b1.place(x=50,y=420,width=200)


        # img1=Image.open("college_images/loginpng.png")
        # img1=img1.resize((200,45),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("arial",15,"bold"),fg="yellow")
        # b1.place(x=330,y=420,width=200)
        b2=Button(frame,text="Login",command=self.return_login,borderwidth=0,cursor="hand2",font=("arial",15,"bold"),bg='blue',fg='yellow')
        b2.place(x=330,y=420,width=200)



    # =================Function declaration============================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Plaese agree our terms ane condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="facial_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,plaese try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()

                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)

    def return_login(self):
        self.root.destroy()
            



if __name__ == "__main__":
    main()
  