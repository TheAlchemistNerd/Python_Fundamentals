from tkinter import *
from PIL import ImageTk, Image   # for handling image files .JPEG, .PNG e.t.c

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('C:/Users/qwert/Desktop/Scripts/Gui/favicon.ico')
button_quit = Button(root, text="Exit Program", command=root.quit) 
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("chlorine.png"))
my_label = Label(root, image = my_img)
my_label.pack()






root.mainloop()