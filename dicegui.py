from tkinter import *
from PIL import ImageTk, Image
import itertools
import random

background_color = "#0D865D"
root = Tk()
root.geometry("960x720")
First_img_path = "./0.png."
Second_img_path = "./0.png"

first_dice = ImageTk.PhotoImage(Image.open(First_img_path))
first_dice_label = Label(root, image=first_dice, bg=background_color)
first_dice_label.pack()
second_dice = ImageTk.PhotoImage(Image.open(Second_img_path))
second_dice_label = Label(root, image=first_dice, bg=background_color)
second_dice_label.pack()


def roll_dice():
    dice_no = list(range(1, 7))
    combination = list(itertools.product(dice_no, repeat=2))#product method 
    rolled_dice = random.choice(combination)
    return rolled_dice


def update_dice_image():
    rolled_dice = list(roll_dice())
    print(rolled_dice)
    new_first_image_path = "./{}.png".format(rolled_dice[0])
    new_second_image_path = "./{}.png".format(rolled_dice[1])

    new_first_dice_image = ImageTk.PhotoImage(Image.open(new_first_image_path))
    new_second_dice_image = ImageTk.PhotoImage(Image.open(new_second_image_path))

    first_dice_label.configure(image=new_first_dice_image)
    second_dice_label.configure(image=new_second_dice_image)

    first_dice_label.image = new_first_dice_image
    second_dice_label.image = new_second_dice_image


roll_button = Button(root, text="roll dices...", command=update_dice_image)
roll_button.pack(side=BOTTOM)

root.configure(bg=background_color)

root.mainloop()
