#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mayur
#
# Created:     31/05/2023
# Copyright:   (c) mayur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from tkinter import *
from tkinter import messagebox

import base64
screen = Tk()
screen.geometry("420x420")
screen.wm_title("encryption and decription  PROJECT by SCOE STUDENTS")
screen.configure(bg="grey")
def encrypt():
    password=code.get()
    if password == "abhi":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x150")
        screen1.configure(bg="maroon")

        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text="MESSAGE IS ENCRYPTED",font="calibri 15 bold").place(x=6,y=7)
        text2 = Text(screen1,font="30",bd=5,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("Error","enter the private key")

    elif(password!="abhi"):
        messagebox.showerror("opps","private key dind't matched")
def decrypt():
    password=code.get()
    if password == "abhi":
        screen2=Toplevel(screen)
        screen2.title("encryption")
        screen2.geometry("400x150")
        screen2.configure(bg="black")

        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2,text="MESSAGE IS ENCRYPTED",font="calibri 15 bold").place(x=6,y=7)
        text2 = Text(screen2,font="30",bd=5,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("Error","enter the private key")
    elif password!="abhi":
        messagebox.showerror("opps","private key dind't matched")

#label
Label(screen,text="Enter The Message To  ENCRYPT OR DECRYPT",font="calibri 13 bold",bg="white").place(x=8,y=9)
#text
text1=Text(screen,font="20")
text1.place(x=5,y=45,width=410,height=120)
#label
Label(screen,text="Enter Secret Key",font="arial 12 bold").place(x=150,y=185)
#entry
code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=100,y=228)
#mini icon
Button(screen,text="ENCRYPT",font="arial 15 bold",bg="red",fg="white",command=encrypt).place(x=15,y=280)
Button(screen,text="DECRYPT",font="arial 15 bold",bg="green",fg="white",command=decrypt).place(x=300,y=280)
Button(screen,text="EXIT",font="arial 10 bold",bg="white").place(x=350,y=180)
Button(screen,text="RESET",font="arial 14 bold",bg="black",fg="white").place(x=70,y=360,width=280,height=40)


mainloop()