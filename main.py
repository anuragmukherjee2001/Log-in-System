import tkinter
from tkinter import ttk
from PIL import Image, ImageTk

class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1650x700+0+0")
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

        first_name_entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        first_name_entry.place(
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

        last_name_entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        last_name_entry.place(
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

        Email_Entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        Email_Entry.place(
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

        contact_entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        contact_entry.place(
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

        Security_Question_box = ttk.Combobox(
                                    frame_1,
                                    font = ("Times New Roman", 12), 
                                    state = 'readonly',
                                    justify = tkinter.CENTER,                         
        )                                                        

        Security_Question_box['values'] = ("Select", "Your First School", "Your Favourite book", "Your Pet name", "Your Best Friend", "Your Favourite Subject")

        Security_Question_box.place(x = 50, y = 270, width = 250)

        Security_Question_box.current(0)

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

        Security_answer_Entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        Security_answer_Entry.place(
                                x = 370,
                                y = 270,
                                width = 250,
                                )

        # Row 4
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

        Password_Entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        Password_Entry.place(
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

        confirm_password_Entry = tkinter.Entry(
                                    frame_1,
                                    font = ("Times New Roman", 15),  
                                    bg = "lightgray",                          
        )                                                        

        confirm_password_Entry.place(
                                x = 370,
                                y = 340,
                                width = 250,
                                )

        # creating the checkbox

        check_box = tkinter.Checkbutton(
                                frame_1,
                                text = "I agree with the terms and conditions",
                                onvalue = 1,
                                offvalue = 0,
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
                                cursor = "hand2",
                                ) 

        login_button.place(
                        x = 200,
                        y = 460,
                        width = 150,
                        height = 40,
                        )   

root = tkinter.Tk()

r1 = Registration(root)

root.mainloop()