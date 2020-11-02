import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import pymysql

class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form".center(370))
        self.root.geometry("1250x700+0+0")
        self.root.resizable(0,0)
        self.root.config(bg = "white")

        #setting the Images

        self.back = ImageTk.PhotoImage(file = "Images/bg.jpg")
        back = tkinter.Label(
                        self.root,
                        image = self.back,
                        )

        back.place(x = 250,
                    y = 0,
                    relwidth = 1,
                    relheight = 1,
                    )

        self.left = ImageTk.PhotoImage(file = "Images/sides.jpg")
        
        left = tkinter.Label(
                        self.root,
                        image = self.left,
                        )
        
        left.place(x = 80,
                    y = 100,
                    width = 400,
                    height = 500,
                  )

        #creating a frame

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

        title = tkinter.Label(
                        frame_1,
                        text = "Register Now",
                        font = ("Helvitica", 20, "bold"),
                        bg = "white",
                        fg = "green",
                        )

        title.place(x = 50, y = 30) 

        #creating the first name 

        first_name = tkinter.Label(
                        frame_1,
                        text = "First Name",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        first_name.place(
                        x = 50,
                        y = 100,
                        )    

        self.first_name_entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.first_name_entry.place(
                            x = 50, 
                            y = 130, 
                            width = 250,
                            )

        # creating the last name

        last_name = tkinter.Label(
                        frame_1,
                        text = "Last Name",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        last_name.place(
                        x = 370, 
                        y = 100,
                        )    

        self.last_name_entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.last_name_entry.place(
                        x = 370, 
                        y = 130, 
                        width = 250,
                        )

        #Creating the Email box

        Email = tkinter.Label(
                        frame_1,
                        text = "Email",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        Email.place(
                    x = 50,
                    y = 170
                    )    

        self.Email_Entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.Email_Entry.place(
                        x = 50, 
                        y = 200, 
                        width = 250
                        )

        #contact number

        contact = tkinter.Label(
                        frame_1,
                        text = "Contact Number",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        contact.place(
                    x = 370,
                    y = 170
                    )    

        self.contact_entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.contact_entry.place(
                            x = 370,
                            y = 200,
                            width = 250
                            )

        # Security Question

        Security_Question = tkinter.Label(
                        frame_1,
                        text = "Security Question",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        Security_Question.place(
                                x = 50,
                                y = 240,
                                )    

        self.Security_Question_box = ttk.Combobox(
                                    frame_1,
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
                                        y = 270, 
                                        width = 250,
                                        )

        self.Security_Question_box.current(0)

        # Security answer

        Security_answer = tkinter.Label(
                        frame_1,
                        text = "Security Answer",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        Security_answer.place(
                            x = 370,
                            y = 240,
                            )    

        self.Security_answer_Entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.Security_answer_Entry.place(
                                x = 370,
                                y = 270,
                                width = 250,
                                )

        #Password

        Password = tkinter.Label(
                        frame_1,
                        text = "Password",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        Password.place(
                        x = 50,
                        y = 310,
                        )    

        self.Password_Entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.Password_Entry.place(
                            x = 50,
                            y = 340,
                            width = 250,
                            )

        #confirm Password

        confirm_password = tkinter.Label(
                        frame_1,
                        text = "Confirm Password",
                        font = ("Times New Roman", 14),
                        bg = "white",
                        fg = "black",
                        )      

        confirm_password.place(
                            x = 370,
                            y = 310,
                            )    

        self.confirm_password_Entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        self.confirm_password_Entry.place(
                                x = 370,
                                y = 340,
                                width = 250,
                                )

        # creating the checkbox

        self.check_done = tkinter.IntVar()

        check_box = tkinter.Checkbutton(
                                frame_1,
                                text = "I agree with the terms and conditions",
                                onvalue = 1,
                                offvalue = 0,
                                variable = self.check_done,
                                bg = "white",
                                font = ("Times New Roman", 12),
                                )

        check_box.place(
                    x = 50,
                    y = 380,
                    )  

        # Register button                             
                          
        Register_button = tkinter.Button(
                                frame_1,
                                text = "Register",
                                font = ("Helvitica", 13),
                                bg = "blue",
                                fg = "white",
                                cursor = "hand2",
                                command = self.data_entry,
                                )  

        Register_button.place(
                        x = 50,
                        y = 420,
                        width = 150,
                        height = 40,
                        )  

        login_button = tkinter.Button(
                                self.root,
                                text = "Sign In",
                                font = ("Helvitica", 13),
                                bg = "blue",
                                fg = "white",
                                command = self.redirect_to_login,
                                cursor = "hand2",
                                ) 

        login_button.place(
                        x = 200,
                        y = 460,
                        width = 150,
                        height = 40,
                        ) 

    def clear_all(self):
      self.first_name_entry.delete(0, tkinter.END)                    
      self.last_name_entry.delete(0, tkinter.END)                    
      self.Email_Entry.delete(0, tkinter.END)                    
      self.contact_entry.delete(0, tkinter.END)                    
      self.Security_Question_box.current(0)                    
      self.Security_answer_Entry.delete(0, tkinter.END)                    
      self.Password_Entry.delete(0, tkinter.END)                    
      self.confirm_password_Entry.delete(0, tkinter.END)                    

    def data_entry(self):
      if(self.first_name_entry.get() == "" or self.Email_Entry.get()=="" or self.contact_entry.get() == "" or self.Security_Question_box.get() == "Select" or self.Security_answer_Entry.get() == "" or self.Password_Entry.get() == "" or self.confirm_password_Entry.get() == ""):
        messagebox.showerror(
                      "Error",
                      "All Fields are Required",
                      parent = self.root,
                      )

      elif(self.Password_Entry.get() != self.confirm_password_Entry.get()):
        messagebox.showerror(
                        "Password Error",
                        "Password and confirm password are not matched",
                        parent = root,
                        )

      elif(self.check_done.get() == 0):
        messagebox.showerror(
                      "Error",
                      "Please agree with our terms and conditions", 
                      parent = root,
                      )                  

      elif(not (self.contact_entry.get() > "0" and self.contact_entry.get() < "9")):
        messagebox.showerror(
                      "Password Error",
                      "Number is not correct",
                      parent = root,
                    ) 

      else:

        try:
          con = pymysql.connect(
                          host = "localhost", 
                          user = "root", 
                          password = "", 
                          database = "employee"
                          )

          cur = con.cursor()
          
          cur.execute("select * from employee where email = %s", self.Email_Entry.get())
          row = cur.fetchone()

          if row != None:
            messagebox.showerror(
                          "Error",
                          "User already exists. Please try with another email.",
                          parent = self.root,
                          )
          else:  
            cur.execute("insert into employee (first_name,last_name,Email,contact,Security_Question,Security_answer,Password) values (%s,%s,%s,%s,%s,%s,%s)",
                      (self.first_name_entry.get(),
                      self.last_name_entry.get(),
                      self.Email_Entry.get(),
                      self.contact_entry.get(),
                      self.Security_Question_box.get(),
                      self.Security_answer_Entry.get(),
                      self.Password_Entry.get()
                      )
            )

            con.commit()
            con.close()
          
            messagebox.showinfo(
                          "Success", 
                          "Registration Successful", 
                          parent = root
                          )

            self.clear_all()                   

        except Exception as ex:
          messagebox.showerror(
                            "Error", 
                            f"Error due to:  {str(ex)}", 
                            parent = self.root
                            )

    def redirect_to_login(self):
      self.root.destroy()
      import login      


root = tkinter.Tk()

r1 = Registration(root)

root.mainloop()