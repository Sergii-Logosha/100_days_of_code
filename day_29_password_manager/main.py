# 14.10.2023 Sergii Logosha sergiilogosha@gmail.com

from tkinter import *

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

email_u_name_label = Label(text='Email/Username:')
email_u_name_label.grid(row=2, column=0, sticky='e')
email_u_name_entry = Entry(width=39)
email_u_name_entry.grid(row=2, column=1, columnspan=2, sticky='w')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0, sticky='e')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')
generate_button = Button(text='Generate Password')
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')

window.mainloop()
