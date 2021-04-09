import tkinter  as tk
import SignLaguage as sn
import Sign_language_Letters as snl
root = tk.Tk()
n=False

def words():
        sn.signlanguage()


def letters():
    snl.letters()

def Exit():
    exit()

filename = tk.PhotoImage(file = "Bg.png")
root.geometry("300x500+10+20")
#root.configure(bg='black')
btn1 = tk.PhotoImage(file = r"button.png")
btn2 = tk.PhotoImage(file = r"button1.png")
btn3 = tk.PhotoImage(file = r"button3.png")

myButton = tk.Button(root,image = filename,borderwidth=0)
myButton.pack(pady=20)
myButton1 = tk.Button(root, command=words,image = btn1,borderwidth=0)
myButton1.pack(pady=20)
myButton2 = tk.Button(root, command=letters,image = btn2,borderwidth=0)
myButton2.pack(pady=20)
myButton3 = tk.Button(root, command=Exit,image = btn3,borderwidth=0)
myButton3.pack(pady=20)
#myButton = Button(root, text="Signlanguage",state=DISABLED)
root.mainloop()