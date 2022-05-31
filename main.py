import pandas as pd
import numpy as np
from tkinter import *
from sklearn.naive_bayes import GaussianNB


def predict():
    # _.config(state = "normal")
    df = pd.read_csv("df.csv")
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    cls = GaussianNB()
    cls.fit(X, y)

    if clicked.get() == "King's Indian Defense":
        c = 4
    elif clicked.get() == "French Defense":
        c = 2
    elif clicked.get() == "London System":
        c = 5
    elif clicked.get() == "Caro-Kann Defense":
        c = 0
    elif clicked.get() == "Scotch Game":
        c = 8
    elif clicked.get() == "Slav Defense":
        c = 7
    elif clicked.get() == "Italian Game":
        c = 3
    elif clicked.get() == "English Opening":
        c = 1
    elif clicked.get() == "Queen's Gambit Declined":
        c = 6

    inp = np.asarray([int(w_elo.get()), int(b_elo.get()), c]).reshape(1, -1)
    # _.config(state = "disabled")
    _.delete(0, last = 20)
    if cls.predict(inp) == 1:
        # _.insert(0, str(cls.predict(inp)))
        _.insert(0, "White should win...")
    elif cls.predict(inp) == -1:
        _.insert(0, "Black should win...")
    else:
        _.insert(0, "Should be draw...")




root = Tk()
root.geometry("800x450")
root.resizable(0, 0)
root.title("Chess Win Predictor")
root.iconbitmap("icon.ico")

bgimg = PhotoImage(file = "bg.ppm")
limg = Label(root, i=bgimg)
limg.place(x = 0, y = 0)

f = Frame(root, bg = '#b73532')

l1 = Label(f, text = "White's Elo:")
l1.grid(row = 0, column = 0)

w_elo = Entry(f)
w_elo.grid(row = 0, column = 1, sticky='ew', ipady = 7, pady = 5)

l2 = Label(f, text = "Black's Elo:")
l2.grid(row = 1, column = 0)

b_elo = Entry(f)
b_elo.grid(row = 1, column = 1, ipady = 7, pady = 5)

l3 = Label(f, text = "Select Opening:")
l3.grid(row = 2, column = 0)

clicked = StringVar()
options = [
    "King's Indian Defense",
    "French Defense",
    "London System",
    "Caro-Kann Defense",
    "Scotch Game",
    "Slav Defense",
    "Italian Game",
    "English Opening",
    "Queen's Gambit Declined"
]
drop = OptionMenu(f , clicked , *options)
drop.grid(row = 2, column = 1, ipady = 7, pady = 5)

Button(f, text = "Predict", command = predict).grid(row = 3, column = 0, ipady = 10, pady = 5)

_ = Entry(f)
_.insert(0, "Prediction!")
_.grid(row = 3, column = 1)
# _.config(state = "disabled")

f.place(x = 275, y = 3)

root.mainloop()

df = pd.read_csv("Chess.csv")
