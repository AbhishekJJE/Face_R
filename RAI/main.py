from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # first image
        img=Image.open(r"bg img\banner.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1 = Image.open(r"bg img\banner.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"bg img\banner.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image
        img3 = Image.open(r"bg img\poster.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)


        title_lbl=Label(bg_img,text="Face Recognition Attendace System Software",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4 = Image.open(r"bg img\studentposter.jpg")
        img4 = img4.resize((170, 170), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4)
        b1.place(x=100,y=75,width=170,height=170)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=100,y=245,width=170,height=40)

        # Face Recognition button
        img5 = Image.open(r"bg img\FRposter.jpg")
        img5 = img5.resize((170, 170), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5)
        b1.place(x=300, y=75, width=170, height=170)

        b1_1 = Button(bg_img, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=300, y=245, width=170, height=40)

        # Attendance button
        img6 = Image.open(r"bg img\attendaceposter.jpg")
        img6 = img6.resize((170, 170), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6)
        b1.place(x=500, y=75, width=170, height=170)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=500, y=245, width=170, height=40)

        # Help button
        img7 = Image.open(r"bg img\helpposter.jpg")
        img7 = img7.resize((170, 170), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7)
        b1.place(x=700, y=75, width=170, height=170)

        b1_1 = Button(bg_img, text="Help", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=700, y=245, width=170, height=40)

        # train button
        img8 = Image.open(r"bg img\studentposter.jpg")
        img8 = img8.resize((170, 170), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8)
        b1.place(x=100, y=320, width=170, height=170)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=100, y=495, width=170, height=40)

        # photo button
        img9 = Image.open(r"bg img\FRposter.jpg")
        img9 = img9.resize((170, 170), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9)
        b1.place(x=300, y=320, width=170, height=170)

        b1_1 = Button(bg_img, text="Photo", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=300, y=495, width=170, height=40)

        # developer button
        img10 = Image.open(r"bg img\attendaceposter.jpg")
        img10 = img10.resize((170, 170), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10)
        b1.place(x=500, y=320, width=170, height=170)

        b1_1 = Button(bg_img, text="Deveplor", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=500, y=495, width=170, height=40)

        # Exit button
        img11 = Image.open(r"bg img\helpposter.jpg")
        img11 = img11.resize((170, 170), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11)
        b1.place(x=700, y=320, width=170, height=170)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=700, y=495, width=170, height=40)















if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()