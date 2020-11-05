import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
# import login

import pymysql

class password:
    def __init__(self, root):
        self.root = root
        self.root.title("Forget Password".center(80))
        self.root.geometry("350x480+400+50")
        self.root.resizable(0,0)
        self.root.config(bg = "white")
        self.root.focus_force()
        self.root.grab_set()    

        title = tkinter.Label(
                            self.root,
                            text = "Forget Password",
                            font = ("Helvitica", 20, "bold"),
                            bg = "white",
                            fg = "green",
                            )

        title.place(
                    x = 0,
                    y = 10,
                    relwidth = 1,
                    # relheight = 1,
                    )

        Security_Question = tkinter.Label(
                        self.root,
                        text = "Security Question",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        Security_Question.place(
                                x = 50,
                                y = 70,
                                )              

        self.Security_Question_box = ttk.Combobox(
                                    self.root,
                                    font = ("Times New Roman", 12), 
                                    state = 'readonly',
                                    justify = tkinter.CENTER,                         
        )                                                        

        self.Security_Question_box['values'] = (
                                              "Select",
                                              "Your First School",
                                              "Your Favourite book",
                                              "Your Pet name", 
                                              "Your Best Friend", 
                                              "Your Favourite Subject",
                                              )

        self.Security_Question_box.place(
                                        x = 50, 
                                        y = 100, 
                                        width = 250,
                                        )

        self.Security_Question_box.current(0)

        Security_answer = tkinter.Label(
                        self.root,
                        text = "Security Answer",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        Security_answer.place(
                            x = 50,
                            y = 150,
                            )    

        self.Security_answer_Entry = tkinter.Entry(
                                    self.root,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.Security_answer_Entry.place(
                                x = 50,
                                y = 180,
                                width = 250,
                                )   

        new_password = tkinter.Label(
                        self.root,
                        text = "New Password",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        new_password.place(
                            x = 50,
                            y = 230,
                            )    

        self.new_password_Entry = tkinter.Entry(
                                    self.root,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.new_password_Entry.place(
                                x = 50,
                                y = 260,
                                width = 250,
                                ) 

        confirm_password = tkinter.Label(
                        self.root,
                        text = "Confirm Password",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        confirm_password.place(
                            x = 50,
                            y = 310,
                            )    

        self.confirm_password_Entry = tkinter.Entry(
                                    self.root,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.confirm_password_Entry.place(
                                x = 50,
                                y = 340,
                                width = 250,
                                ) 

        login_button = tkinter.Button(
                                self.root,
                                text = "Reset Password",
                                font = ("Helvitica", 15),
                                bg = "blue",
                                fg = "white",
                                command = self.forget_password_logic,
                                cursor = "hand2",
                                ) 

        login_button.place(
                        x = 80,
                        y = 410,
                        width = 180,
                        height = 40,
                        )  

                                                                           
    def forget_password_logic(self):
        if self.Security_Question_box.get() == "Select" or self.Security_answer_Entry.get() == "" or self.new_password_Entry.get() == "" or self.confirm_password_Entry.get() == "":
            messagebox.showerror(
                            "Error", 
                            "All fields are required", 
                            parent = self.root,
                            )

        else:
            con = pymysql.connect(
                                    host = "localhost",
                                    user = "root",
                                    password = "",
                                    database = "employee",
                                    )

            cur = con.cursor()
            cur.execute("select * from employee where Email = %s", login.email_entry.get())

            row = cur.fetchone()
                 
            if row == None:
                messagebox.showerror(
                                    "Error",
                                    "Please enter a valied email address to reset the password",
                                    parent = self.root
                                    )                    
            

root = tkinter.Tk()

f1 = password(root)

root.mainloop()