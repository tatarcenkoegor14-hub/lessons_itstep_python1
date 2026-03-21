import tkinter as tk


score = 0
click_power = 1
auto_income = 0

def update_labels():
    score_label.config(text=f"Очки: {score}")
    power_label.config(text=f"Сила кліку: {click_power}")
    auto_label.config(text=f"Авто-дохід: {auto_income}/сек")

def click():
    global score
    score += click_power
    update_labels()

def upgrade_click():
    global score, click_power
    if score >= 10:
        score -= 10
        click_power += 1
        update_labels()

def upgrade_auto():
    global score, auto_income
    if score >= 20:
        score -= 20
        auto_income += 1
        update_labels()

def auto_gain():
    global score
    score += auto_income
    update_labels()
    root.after(1000, auto_gain)


root = tk.Tk()
root.title("Клікер гра")


score_label = tk.Label(root, text="Очки: 0", font=("Arial", 16))
score_label.pack()

power_label = tk.Label(root, text="Сила кліку: 1")
power_label.pack()

auto_label = tk.Label(root, text="Авто-дохід: 0/сек")
auto_label.pack()

# Кнопки
click_button = tk.Button(root, text="КЛІК!", font=("Arial", 14), command=click)
click_button.pack(pady=10)

upgrade_click_btn = tk.Button(root, text="Покращити клік (10)", command=upgrade_click)
upgrade_click_btn.pack()

upgrade_auto_btn = tk.Button(root, text="Купити авто (20)", command=upgrade_auto)
upgrade_auto_btn.pack()


root.after(1000, auto_gain)


root.mainloop()