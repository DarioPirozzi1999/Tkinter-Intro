from tkinter import *

root = Tk()

root.geometry("250x250")
root.title("Challenge")

btnLeft = Button(root, text = "Click here",background = "green", bd = 5, command = root.destroy)
btnRight = Button(root, text = "Click here",background = "green", bd = 5, command = root.destroy)
btnUp = Button(root, text = "Click here",background = "green", bd = 5, command = root.destroy)
btnDown = Button(root, text = "Click here",background = "green", bd = 5, command = root.destroy)

btnDown.pack(side="bottom")
btnUp.pack(side="top")
btnRight.pack(side="right")
btnLeft.pack(side="left")

root.mainloop()
