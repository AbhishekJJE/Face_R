from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Fasce_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        img=Image.open(r"image path")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)









if __name__== "__main__":
    root=Tk()
    obj=Fasce_Recognition_System(root)
    root.mainloop()