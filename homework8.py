import tkinter as tk


clicks = 0


def click():
    global clicks
    clicks += 1
    label.config(text=f"Кліки: {clicks}")


window = tk.Tk()
window.title("Гра-клікер")
window.geometry("300x200")


label = tk.Label(window, text="Кліки: 0", font=("Arial", 20))
label.pack(pady=20)


button = tk.Button(window, text="Клікни мене", font=("Arial", 16), command=click)
button.pack(pady=10)


window.mainloop()