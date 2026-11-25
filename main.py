from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_number + password_symbol + password_letter

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0,password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = Em_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error",message="You must fill all fields")


    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}\n"
                                                  f"Password: {password} \nis it ok to save?")
        if is_ok:
            with open("data.txt" , "a") as f:
                f.write(f"website: {website} || Email: {email} || Password: {password}\n")
                website_del = web_entry.delete(0,END)
                email_del = Em_entry.delete(0,END)
                password_del = pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(130,100,image=logo)
canvas.grid(row=0,column=1)

#Labels
web_label = Label(text="Website:")
web_label.grid(row=1 , column=0)

Em_label = Label(text="Email/Username:")
Em_label.grid(row=2 , column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3 , column=0)

#Entries
web_entry = Entry(width=45)
web_entry.grid(row=1 , column=1 , columnspan=2 , sticky="ew")

web_entry.focus() # cursor is ready
Em_entry = Entry(width=45)
Em_entry.grid(row=2,column=1 , columnspan=2 , sticky="ew")
pass_entry = Entry(width=25)
pass_entry.grid(row=3 , column=1 , sticky="ew")

#Button

generate_button = Button(text="Generate Password", width=21 , command=password_generate)
generate_button.grid(row= 3, column=2)

add_button =Button(text="Add" , width=50 , command=save)
add_button.grid(row=4,column=1 , columnspan=2)




















window.mainloop()