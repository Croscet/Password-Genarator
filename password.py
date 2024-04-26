import secrets
from tkinter import *
import string

def new_rand():
    if (x.get())==0 and (y.get())==0:
         try:
               bolo = (string.ascii_letters + string.digits + string.punctuation)

               password_entry.delete(0,END)
               pw_length=int(my_entry.get())
               my_pass=' '
               for i in range(pw_length):

                my_pass += (str((secrets.choice(bolo))))
               password_entry .insert(0,my_pass)
               password_entry.delete(1+pw_length,END)
         except ValueError:
             Error='Error'
             password_entry.delete(0,END)
             password_entry.insert(0,Error)


    if (x.get()) == 1 and (y.get()) == 1:
         try:
                bolo = (string.ascii_letters )

                password_entry.delete(0, END)
                pw_length = int(my_entry.get())
                my_pass = ''
                for i in range(pw_length):
                 my_pass += (str((secrets.choice(bolo))))
                 password_entry.insert(0, my_pass)
                 password_entry.delete(1 + pw_length, END)
         except ValueError:
                Error = 'Error'
                password_entry.delete(0, END)
                password_entry.insert(0, Error)


    if (x.get()) == 1 and (y.get()) == 0:
         try:
                bolo = (string.ascii_letters + string.punctuation)

                password_entry.delete(0, END)
                pw_length = int(my_entry.get())
                my_pass = ''
                for i in range(pw_length):
                 my_pass += (str((secrets.choice(bolo))))
                 password_entry.insert(0, my_pass)
                 password_entry.delete(1 + pw_length, END)
         except ValueError:
                Error = 'Error'
                password_entry.delete(0, END)
                password_entry.insert(0, Error)

    if (x.get()) == 0 and (y.get()) == 1:
         try:
                bolo = (string.ascii_letters + string.digits)

                password_entry.delete(0, END)
                pw_length = int(my_entry.get())
                my_pass = ''
                for i in range(pw_length):
                 my_pass += (str((secrets.choice(bolo))))
                 password_entry.insert(0, my_pass)
                 password_entry.delete(1 + pw_length, END)
         except ValueError:
                Error = 'Error'
                password_entry.delete(0, END)
                password_entry.insert(0, Error)




def Copy():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())


window=Tk()

x=IntVar()

y=IntVar()

window.geometry('500x500')


image1=PhotoImage(file='confetti2.PNG')
window.title('Password Generator')

Label1=Label(window,image=image1)
Label1.place(x=125,y=0)

label=Label(window,text='Welcome to Password Generator',font=('Comic Sans',25),fg='Red')
label.pack(padx=20,pady=20)

frame=Frame(window,bg='#848fdf')
frame.pack()

Jol=LabelFrame(window,text='How many characters?',font=('Arial',20),bg='#63fe92')
Jol.pack(pady=30,padx=0)

my_entry=Entry(Jol,font=('Helvetica',25))
my_entry.pack()

password_entry=Entry(window,font=('Helvetica',20),width=50,fg='#004080',borderwidth=2)
password_entry.pack(pady=30,padx=5)

checkbox1=Checkbutton(frame,onvalue=0,offvalue=1,variable=x,text='Include Numbers',font=('Arial',20),fg='Dark violet',width=30)
checkbox1.grid(row=0,column=0,pady=5)

checkbox2=Checkbutton(frame,onvalue=0,offvalue=1,variable=y,text='Include Special characters',font=('Arial',20),fg='Dark green')
checkbox2.grid(row=1,column=0,pady=5)

my_button=Button(window,text='Generate  Password',font=('Arial',20),command=new_rand,fg='#0c7b9c')
my_button.pack()

clip_button=Button(window,text='Copy to Clipboard'.upper(),font=('Comic Sans',20),command=Copy,fg='brown')
clip_button.pack()

window.mainloop()
