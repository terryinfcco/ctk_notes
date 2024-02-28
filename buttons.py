import customtkinter
import tkinter

# Set the theme (choices: light, dark, system)
customtkinter.set_appearance_mode("dark")

# Set the default color mode - choices he showed: green, blue
customtkinter.set_default_color_theme("green")

# Create the desktop window and call it app
app = customtkinter.CTk()

# Add a title to the window
app.title("Button App by Turtle Code")

# Set the size of the window (widthxheight)
app.geometry("300x300")

# function to be executed when button is clicked
def button_function():
    print("button pressed!")

# Create button variable - window where it should appear, button text, and function to execute when clicked
button = customtkinter.CTkButton(master=app, text="CTKBUTTON", command=button_function)
button.place(relx=0.5, rely=0.8, anchor = tkinter.CENTER)
app.mainloop()