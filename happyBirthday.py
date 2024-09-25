import tkinter as tk


def happy_birth day():
    window = tk.Tk()
    window.title("HaPpY BiRtHdAy")


    canvas = tk.Canvas(window,width=200,height=200)
    canvas.pack()

    canvas.create_polygon(100, 50, 150, 100, 100, 150, 50, 100, fill="red")

    canvas.create_text(100, 125, text="HaPpY biRtHdAy", fill="white")

    window.mainloop()

happy_birthday()