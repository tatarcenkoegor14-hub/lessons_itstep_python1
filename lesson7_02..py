import tkinter as tk

root = tk.Tk()
root.title("GUI tkinter")
#root.iconbitmap("image.ico")
root.geometry("640x480")
root.resizable(False, False)
root.minsize(320, 240)
root.maxsize(1920, 1080)

label_title = tk.Label(root, text="Hello Student",
                       font=("Arial", 24, "bold italic"),
                       fg="32557F",
                       bg="3D1035",
                       width=20,
                       height=3,
                       anchor="center",
                       relief="solid",
                       bd=5,
                       justify= "left",
                       )
label_title.pack()

button_play = tk.Button(master=root,
                        text="Click me",
                        font=("Arial", 24, "bold italic"),
                        fg="709172",
                        bg="3D1035",
                        width=30,
                        height=3,
                        anchor="center",
                        relief="solid",
                        )
button_play.pack()

img =tk.PhotoImage(file="img.png")
label_img = tk.Label(master=root,
                     image=img,
                     )
root.mainloop()