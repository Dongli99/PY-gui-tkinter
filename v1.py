from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# functions
def clickreset():
    namevar.set("Dongli Liu")
    residencyvar.set("dom")
    programcmb.set("AI")
    coursechk1.deselect()
    coursechk2.deselect()
    coursechk3.deselect()


def clickok():
    message = (
        "Name: "
        + namevar.get()
        + "\nResidency: "
        + residencyvar.get()
        + "\nProgram: "
        + programcmb.get()
        + "\nCourses: "
    )
    for var in [coursevar1, coursevar2, coursevar3]:
        if var.get():
            message += "\n  -"
            message += var.get()
    messagebox.showinfo("Student Info", message)


# Declare and set root from tkinter
root = Tk()
root.title("Centennial College")
root.config(background="lightgreen")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

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
namevar = StringVar()
namevar.set("Dongli Liu")
nameentry = Entry(frame, width=25, textvariable=namevar)


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
coursevar1 = StringVar()
coursevar2 = StringVar()
coursevar3 = StringVar()
coursechk1 = Checkbutton(
    frame,
    text="Programming I",
    variable=coursevar1,
    onvalue="COMP100",
    offvalue="",
    bg="lightgreen",
)
coursechk2 = Checkbutton(
    frame,
    text="Web Page Design",
    variable=coursevar2,
    onvalue="COMP213",
    offvalue="",
    bg="lightgreen",
)
coursechk3 = Checkbutton(
    frame,
    text="Software Engineering",
    variable=coursevar3,
    onvalue="COMP120",
    offvalue="",
    bg="lightgreen",
)

# buttons
resetbtn = Button(frame, text="Reset", command=clickreset, width=10)
okbtn = Button(frame, text="Ok", command=clickok, width=10)
exitbtn = Button(frame, text="Exit", command=root.quit, width=10)

# LAYOUT
# 3 parts of root
headerlbl.grid(row=0, column=0)
frame.grid(row=1, column=0)
for i in range(8):
    Frame.rowconfigure(root, i, weight=1)
    Grid.rowconfigure(root, i, weight=1)
for i in range(3):
    Frame.columnconfigure(root, i, weight=1)

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
