import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import pymysql

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window".center(370))
        self.root.geometry("1250x700+0+0")
        self.root.resizable(0,0)
        self.root.config(bg = "dark blue")

        self.left = ImageTk.PhotoImage(file = "Images/bg.jpg")
        
        left = tkinter.Label(
                        self.root,
                        bg = "blue",
                        bd = 0,
                        )

        left.place(x = 0,
                    y = 0,
                    width = 600,
                    relheight = 1,
                    )
        
        right = tkinter.Label(
                        self.root,
                        image = self.left,
                        )
        
        right.place(x = 80,
                    y = 100,
                    width = 400,
                    height = 500,
                  )

        # Creating the frame

        frame_1 = tkinter.Frame(
                                self.root,
                                bg = "white",
                                )

        frame_1.place(
                    x = 480,
                    y = 100,
                    width = 700,
                    height = 500,
                    ) 

        login_button = tkinter.Button(
                                frame_1,
                                text = "Login",
                                font = ("Helvitica", 13),
                                bg = "blue",
                                fg = "white",
                                command = self.login_system,
                                cursor = "hand2",
                                ) 

        login_button.place(
                        x = 50,
                        y = 400,
                        width = 150,
                        height = 40,
                        )   

        title = tkinter.Label(
                        frame_1,
                        text = "Login Here",
                        font = ("Helvitica", 30, "bold"),
                        bg = "white",
                        fg = "green",
                        )

        title.place(
                    x = 50,
                    y = 30
                    )  

        # email

        email = tkinter.Label(
                        frame_1,
                        text = "EMAIL ADDRESS",
                        font = ("Helvitica", 15, "bold"),
                        bg = "white",
                        fg = "black",
                        )  

        email.place(
                x = 50, y = 150,
        )   

        # Email Entry    

        self.email_entry = tkinter.Entry(
                            frame_1,
                            font = ("Helvitica", 15),
                            bg = "light gray", 
                            fg = "black"
                            )                   

        self.email_entry.place(
                                x = 50, 
                                y = 190, 
                                width = 350, 
                                height = 35
                                )

        # password

        password = tkinter.Label(
                        frame_1,
                        text = "PASSWORD",
                        font = ("Helvitica", 15, "bold"),
                        bg = "white",
                        fg = "black",
                        )  

        password.place(
                x = 50, y = 250,
        )

        #password Entry

        self.password_entry = tkinter.Entry(
                            frame_1,
                            font = ("Helvitica", 15),
                            bg = "light gray", 
                            fg = "black"
                            )                   

        self.password_entry.place(
                        x = 50, 
                        y = 290, 
                        width = 350, 
                        height = 35
                        )  

        # Register button 

        Register_button = tkinter.Button(
                                frame_1,
                                text = "Register New Account",
                                font = ("Helvitica", 13),
                                bg = "white",
                                bd = 0,
                                fg = "red",
                                command = self.redirect_to_register,
                                cursor = "hand2",
                                ) 

        Register_button.place(
                        x = 30,
                        y = 330,
                        width = 200,
                        height = 30,
                        )

        forgot_password_button = tkinter.Button(
                                frame_1,
                                text = "Forget Password?",
                                font = ("Helvitica", 13),
                                bg = "white",
                                bd = 0,
                                fg = "red",
                                command = self.redirect_to_forget_password,
                                cursor = "hand2",
                                ) 

        forgot_password_button.place(
                        x = 240,
                        y = 330,
                        width = 200,
                        height = 30,
                        )                

    def login_system(self):
        if self.email_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)

        else:

            try:
                con = pymysql.connect(
                                    host = "localhost",
                                    user = "root",
                                    password = "",
                                    database = "employee",
                                    )

                cur = con.cursor()
                cur.execute("select * from employee where Email = %s and Password = %s", (self.email_entry.get(), self.password_entry.get()))

                row = cur.fetchone()
                 
                if row == None:
                    messagebox.showerror(
                                    "Error",
                                    "INVALIED USERNAME and PASSWORD",
                                    parent = self.root
                                    )                  

                else:
                    messagebox.showinfo(
                                    "SUCCESS", 
                                    "WELCOME", 
                                    parent = root
                                    )

                con.close()                                                  


            except Exception as ex:
                messagebox.showerror("Error", f"Error Due to: {str(ex)}", parent = self.root)

    def redirect_to_register(self):
        self.root.destroy()
        import Register  

    def redirect_to_forget_password(self):
        if self.email_entry.get() == "":
            messagebox.showerror(
                            "Error", 
                            "Enter the valied email to reset your password", 
                            parent = root,
                            )
        else:
            import forget_password                  

root = tkinter.Tk()

l1 = login(root)

root.mainloop()