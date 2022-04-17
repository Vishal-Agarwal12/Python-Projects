from tkinter import *
from tkinter import messagebox
import base64 # Base64 encoding is used to convert bytes that have binary or text data into ASCII characters

screen=Tk()    # making a tkinter instance window
screen.geometry("420x420")
screen.title("Encryption and Decryption")
screen.configure(bg="pink")
# Label Widget = Tkinter Label is a widget that is used to implement display boxes where you can place text or images
label1=Label(screen,text="Enter the text for Encryption and Decryption",font="impack 14 bold",bg="yellow")
label1.place(x=6,y=9)

def encrypt():
    password=code.get()
    if password=="1234" :
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="pink")
        
        message = text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text="Your message is Encrypted",font="impack 20 bold").place(x=5,y=9)
        text2 = Text(screen1,font=3,bd=4,wrap=WORD)
        text2.place(x=3,y=50,width=390,height=180)
        text2.insert(END,encrypt)
        
    elif(password==""):
        messagebox.showerror("Error","Please Enter the Secret Key")
    elif(password!="1234"):
        messagebox.showerror("Oops","Invalid Secret Key")
        
def decrypt():
    password=code.get()
    if password=="1234" :
        screen2=Toplevel(screen)
        screen2.title("Encryption")
        screen2.geometry("400x250")
        screen2.configure(bg="green")
        
        message = text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2,text="Your message is Encrypted",font="impack 20 bold").place(x=5,y=3)
        text2 = Text(screen2,font=3,bd=4,wrap=WORD)
        text2.place(x=3,y=50,width=390,height=180)
        text2.insert(END,encrypt)
        
    elif(password==""):
        messagebox.showerror("Error","Please Enter the Secret Key")
    elif(password!="1234"):
        messagebox.showerror("Oops","Invalid Secret Key")     
        
def reset():
    text1.delete(1.0,END)
    code.set("")        

# Text Widget = Text Widget is used where a user wants to insert multiline text fields
text1=Text(screen,font="20")
text1.place(x=5,y=40,width=410,height=100)

label2=Label(screen,text="Enter Secret Key",font="impack 14 bold",bg="yellow")
label2.place(x=5,y=150)

# Entry Widget = This widget allows the user to enter a single line of text
code=StringVar()
Entry(textvariable=code,bd=4,font=20,show="*").place(x=3,y=185)

# Button Widget =The Button widget is used to add buttons in a Python application. These buttons can display text or images that convey the purpose of the buttons. You can attach a function or a method to a button which is called automatically when you click the button.
Button(screen,text="Encrypt",font="arial 15 bold",bg="red",fg="white",command=encrypt).place(x=3,y=220,width=90)

Button(screen,text="Decrypt",font="arial 15 bold",bg="red",fg="white",command=decrypt).place(x=100,y=220,width=95)

Button(screen,text="Reset",font="arial 15 bold",bg="red",fg="white",command=reset).place(x=200,y=220,width=95)

mainloop()   # a method in the main window that executes what we wish to execute in an application