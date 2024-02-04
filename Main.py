from tkinter import *

window = Tk()

# window size
window.geometry("600x600")
window.maxsize(1920, 1080)
window.minsize(200, 200)

# window title
window.title("Instagram Profile Downloader")

# window label
label = Label(window, text="Hello World")
label.pack()


# hello command
def hello():
    label.config(text=inputs.get())
    # print("Hello World")


def clear():
    inputs.delete(0, END)
    label.config(text="Hello World")


# button design
button = Button(window, text="click here", fg="blue", command=hello)
button.pack()   # we can use button.place(x = n, y = n)

button = Button(window, text="close", fg="red", command=window.quit)
button.place(x=30, y=30)

button = Button(window, text="clear", fg="blue", command=clear)
button.place(x=65, y=30)

# input
inputs = Entry(window)
inputs.place(x=240, y=60)


window.mainloop()
