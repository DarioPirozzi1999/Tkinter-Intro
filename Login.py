from tkinter import *

root = Tk()

root.geometry("500x500")
root.title("LoginPage")
root.config(background = "pink")

username = Label(root, text= "Username").place(x=40, y=60)
usernameEntry = Entry(root, width = 30). place(x = 110, y = 60)
password = Label(root, text = "Password"). place(x = 40, y = 100)
passwordEntry = Entry(root, width = 30, show = '*'). place(x = 110, y = 100)
btn = Button(root, text = "login", bd = 5, background = "gray", command= root.destroy)
btn.place(x =250, y = 300)

root.mainloop()