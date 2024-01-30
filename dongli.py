from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# functions
def handlereset():
    pass


def handlesubmit():
    pass


# Declare and set root from tkinter
root = Tk()
root.title("Centennial College")
root.config(background="lightgreen")


# Create elements on the page
# HEADER
headerlbl = Label(
    root,
    text="ICET Student Survey",
    pady=20,
    bg="lightgreen",
    font=("calibri", 20, "italic", "bold"),
)


# MAIN FRAME to contain widgets
frame = Frame(root, bg="lightgreen", padx=20)

# FIRST COL, labels
fnamelbl = Label(frame, text="Full name: ", bg="lightgreen")
residencylbl = Label(frame, text="Residency: ", bg="lightgreen")
programlbl = Label(frame, text="Program: ", bg="lightgreen")
courselbl = Label(frame, text="Courses: ", bg="lightgreen")


# SECOND COL
# text areas and options
nameentry = Entry(frame, width=25)
nameentry.insert(0, "Dongli Liu")
nameentry

# Residency radio
residencyvar = StringVar()
residencyrdo1 = Radiobutton(
    frame, text="Domestic", variable=residencyvar, bg="lightgreen", value="dom"
)
residencyrdo2 = Radiobutton(
    frame, text="International", variable=residencyvar, bg="lightgreen", value="intl"
)
residencyvar.set("dom")

# program combobox
options = ["AI", "Gaming", "Health", "Software"]
programcmb = ttk.Combobox(frame, values=options)
programcmb.set("AI")
programcmb

# course checkbox
coursechk1 = Checkbutton(
    frame, text="Programming I", onvalue="COMP100", offvalue="", bg="lightgreen"
)
coursechk2 = Checkbutton(
    frame, text="Web Page Design", onvalue="COMP213", offvalue="", bg="lightgreen"
)
coursechk3 = Checkbutton(
    frame, text="Software Engineering", onvalue="COMP120", offvalue="", bg="lightgreen"
)

# BOTTOM FRAME
bottomframe = Frame(root, bg="lightgreen", pady=20, padx=20)
# buttons
resetbtn = Button(bottomframe, text="Reset", command=handlereset, width=10)
okbtn = Button(bottomframe, text="Ok", command=handlesubmit, width=10)
exitbtn = Button(bottomframe, text="Exit", command=root.quit, width=10)

# LAYOUT
# 3 parts of root
headerlbl.grid(row=0, column=0)
frame.grid(row=1, column=0, sticky=W)
bottomframe.grid(row=2, column=0)

# element in the main frame - left
fnamelbl.grid(row=0, column=0, sticky=NW, padx=10, pady=3)
residencylbl.grid(row=1, column=0, sticky=NW, padx=10, pady=3, rowspan=2)
programlbl.grid(row=3, column=0, sticky=NW, padx=10, pady=3)
courselbl.grid(row=4, column=0, sticky=NW, padx=10, pady=3, rowspan=3)
# element in the main frame - right
nameentry.grid(row=0, column=1, sticky=W, padx=10, pady=3)
residencyrdo1.grid(row=1, column=1, sticky=W, padx=10, pady=3)
residencyrdo2.grid(row=2, column=1, sticky=W, padx=10, pady=3)
programcmb.grid(row=3, column=1, sticky=W, padx=10, pady=3)
coursechk1.grid(row=4, column=1, sticky=W, padx=10, pady=3)
coursechk2.grid(row=5, column=1, sticky=W, padx=10, pady=3)
coursechk3.grid(row=6, column=1, sticky=W, padx=10, pady=3)

# element in bottom frame
resetbtn.grid(row=0, column=0, padx=10, pady=5)
okbtn.grid(row=0, column=1, padx=10, pady=5)
exitbtn.grid(row=0, column=2, padx=10, pady=5)

# Show the window
root.mainloop()
