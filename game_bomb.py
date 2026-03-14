from tkinter import *

def start(event):
	global press_return
    global bomb
    global score
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text="")
        update_bomb()
        update_score()
        update_display()
        press_return = False

def update_display():
    global bomb
    global score
    if bomb> 50:
        bomb_label.config(image=normal_photo)
    elif 0 < bomb  <= 50:
        bomb_label.config(image=no_photo)
    elif bomb <= 0:
        bomb_label.config(image=bang_photo)
    fuse_label.config(text="Fuse: "+str(score))
    score_label.config(text="Score: "+str(score))
    fuse_label.after( 100, update_display)

def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(400, update_bomb)

    def update_score():
        global score
        score += 1
    if is_alive():
            score_label.after(30000, update_score)

def click():
    global bomb
    if is_alive():
        bomb += 1

def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        label.config(text="Bang! Bang! Bang!!!")
        press_return = True
        return False
    else:
        return True

bomb =  100
score = 0
press_return = True
best_score = 0


root = Tk()
root.title("Bang! Bang! Bang!!!")
root.geometry("480x640")
root.resizable(True, True)

label = Label(root,
              text ="Press [enter] to start",
              font = ("Cosmic Sans MS", 16, "bold italic"),
              fg = "purple",
              bg = "cyan",
              )
label.pack()

fuse_label = Label(root,
                   text ="Fuse: " + str(bomb),
                   font = ("Cosmic Sans MS", 16, "bold italic"),
                   fg = "purple",
                   bg = "cyan",
                   )
fuse_label.pack()

score_label = Label(root,
                    text = "Score: " + str(score),
                    font = ("Cosmic Sans MS", 16, "bold italic"),
                    fg = "purple",
                    bg = "cyan",
                    )
score_label.pack()
no_photo = PhotoImage(file = "images/bomb_no.gif")
normal_photo = PhotoImage(file = "images/bomb_normal.gif")
bang_photo = PhotoImage(file="img/pow.gif")

bomb_label = Label(root,
                   image=normal_photo,
                   )

bomb_label.pack()

click_button = Button(root,
                      text = "Click me!",
                      font = ("Cosmic Sans MS", 16, "bold italic"),
                      fg = "red",
                      bg = "yellow",
                      width = 20,
                      command=click,
                      )
click_button.pack()

root.bind("<Return>", start)




root.mainloop()




















































