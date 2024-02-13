#importing Libraries

from tkinter import *
import random, string
import pyperclip



###initialize window

root =Tk()
root.geometry("600x600")
root.resizable(0,0)
root.title("Ujjawal project - PASSWORD GENERATOR")

#heading
heading = Label(root, text = 'PASSWORD GENERATOR' ,fg='pink',bg='black', font ='algerian 32 bold').pack()
Label(root, text ='project by Ujjawal', font ='arial 18 bold').pack(side = BOTTOM)



###select password length
pass_label = Label(root, text = 'PASSWORD LENGTH',fg='white',bg='orange', font = 'arial 20 bold').pack(pady='25')
pass_label=Label(root, text = '(min size=8   max size=32 )').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 25).pack()



#####define function

pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
   


###button

Button(root, text = "GENERATE PASSWORD" ,fg='white',bg='maroon',font='aerial' '20' 'bold', command = Generator ).pack(pady= 30)

Entry(root , textvariable = pass_str ).pack()

########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get(width=50))

Button(root, text = 'COPY TO CLIPBOARD',fg='white',bg='green',font='aerial' '40' 'bold', command = Copy_password).pack(pady=25)




# loop to run program
root.mainloop()
