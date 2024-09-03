import tkinter as tk
import tkinter.messagebox as messagebox
import random

move_count = 0

def move_cancel_button():
    global move_count
    move_count += 1
    if move_count >= 15:
        messagebox.showinfo("پیام", "واقعا متاسفم واست")
        move_count = 0
    else:
        new_x = random.randint(100, 400)
        new_y = random.randint(100, 400)
        cancel_button.place(x = new_x, y = new_y)

#def show_second_message():
   # messagebox.showinfo(("پیام", "موافقم"))

root = tk.Tk()
root.title("my game")


header_label = tk.Label(root, text="قبول داری پرسپولیس بهترین تیم ایرانه؟", font=("B Zar", 22))
header_label.pack()


#ok_button = tk.Button(root, text="معلومه", bg="green", fg= "#fff")
#ok_button.pack()

cancel_button = tk.Button(root, text="نه چون یه کیسه کش بدبختم", bg="red", fg= "#fff")
cancel_button.pack()

cancel_button.bind("<Enter>", lambda e : move_cancel_button())
root.mainloop()






























