from tkinter import *

root = Tk()  # root widget

def myClick():
	myLabel = Label(root, text = "Look! I clicked a Button!")
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="#000000")
myButton.pack()


 
root.mainloop()