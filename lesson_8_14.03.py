import tkinter as tk
import re

login_pattern = re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
password_pattern = re.compile(r"^\w{8,16}$")

def logining():



def logining():
    login = login_entry.get()
    password = password_entry.get()
    if login_pattern.search(login):
        if login_pattern.search(password):
            login_entry.config(bg="green")
            password_entry.config(bg="green")
        else:
            login_entry.config(bg="red")
            password_entry.config(bg="red")
    else:
        login_entry.config(bg="red")
        password_entry.config(bg="red")

root = tk.Tk()
root.title("Logining")
root.geometry("640x480")
root.resizable(width=True, height=True)


login_label = tk.Label(root,
                       text="Login",
                       font=("Comic Sans MC", 16, "bold italic"),
                       fg="black",
                       bg="yellow",
                       )
login_entry = tk.Entry(root,
                       font=("Comic Sans MC", 14, "bold italic"),
                       bg="yellow",
                       width=30,
                       )
password_label = tk.Label(root,
                          text="Password",
                          font=("Comic Sans MC", 14, "bold italic"),
                          fg="black",
                          bg="yellow",
                          )
password_entry = tk.Entry(root,
                          font=("Comic Sans MC", 14, "bold italic"),
                          bg="yellow",
                          width=30,
                          show="*",
                           )
login_button = tk.Button(root,
                         text="Login",
                         font=("Comic Sans MC", 14, "bold italic"),
                         fg="red",
                         bg="yellow",
                         width=15,
                         command=logining,
                         )
root.grid_columnconfigure(0, minsize=250)
root.grid_columnconfigure(1, minsize=250)
root.grid_rowconfigure(0, minsize=90)
root.grid_rowconfigure(1, minsize=90)

login_button.grid(columnspan=2)

login_label.grid(column=0, row=0, sticky="w")
password_label.grid(column=0, row=1, sticky="w")
login_entry.grid(column=1, row=0, sticky="w")
password_entry.grid(column=1, row=2, sticky="w")
login_button.grid(column=0, row=2,)





root.mainloop()




