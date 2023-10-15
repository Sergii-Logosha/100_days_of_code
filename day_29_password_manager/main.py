# 14.10.2023 Sergii Logosha sergiilogosha@gmail.com
# Last modified 15.10.2023

from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip


def save():
    user_website = website_entry.get()
    user_email_username = email_u_name_entry.get()
    user_password = password_entry.get()

    if user_website == '' or user_password == '' or user_email_username == '':
        messagebox.showinfo(title='Oops', message="Please, don't leave any "
                                                  "fields empty")
    else:
        is_ok = messagebox.askokcancel(title=user_website,
                                       message=f'Credentials to be saved:\n'
                                       f'Email/Username: {user_email_username}'
                                       f'\nPassword: {user_password}\n'
                                       f'Do you want to save it?')

        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f'{user_website} | {user_email_username} | '
                           f'{user_password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)


window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0, sticky='e')
website_entry = Entry(width=39)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()

email_u_name_label = Label(text='Email/Username:')
email_u_name_label.grid(row=2, column=0, sticky='e')
email_u_name_entry = Entry(width=39)
email_u_name_entry.grid(row=2, column=1, columnspan=2, sticky='w')
email_u_name_entry.insert(0, 'sergiilogosha@gmail.com')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0, sticky='e')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')

window.mainloop()
