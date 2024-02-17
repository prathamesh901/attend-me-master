from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        help_bt = Button(f_lbl, text="Send Mail", cursor="hand2", font=("times new roman", 18, "bold"), bg="red",
                         fg="white", command=self.open_gmail)
        help_bt.place(x=370, y=473, width=195, height=65)

    def open_gmail(self):
        # Specify the recipient email address, subject, and body
        recipient = "prathameshhh901@gmail.com"
        subject = "Subject"
        body = "Body"

        # Compose the mailto URL with the specified parameters
        mailto_url = f"mailto:{recipient}?subject={subject}&body={body}"

        # Open the default web browser with the Gmail URL
        webbrowser.open(mailto_url)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()

