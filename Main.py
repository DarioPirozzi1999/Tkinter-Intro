from tkinter import *

root = Tk()

root.geometry("250x250")
root.title("First Project")

btn = Button(root, text= "click here !",bd= 5, background = "green",command = root.destroy)

btn.pack(side = "bottom")

root.mainloop()