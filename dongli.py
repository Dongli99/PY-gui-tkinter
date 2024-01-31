from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont
from tkinter import messagebox


class SurveyGUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Centennial College")
        self.create_styles()
        Canvas(self, width=480, height=360).pack()
        containter = Frame(self)
        containter["relief"] = "ridge"
        containter.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.create_variables()
        self.init_ui()
        self.create_ui(containter)

    def create_styles(self):
        style = Style()
        style.theme_use("clam")
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=10)

    def create_variables(self):
        self.name = StringVar()
        self.residency = StringVar()
        self.program = StringVar()

        self.course1 = StringVar()
        self.course2 = StringVar()
        self.course3 = StringVar()

        self.programs = ["AI", "Gaming", "Health", "Software"]
        self.courses = [self.course1, self.course2, self.course3]

    def init_ui(self):
        self.name.set("Dongli Liu")
        self.residency.set("dom")
        self.program.set("AI")
        for course in self.courses:
            course.set("")

    def create_ui(self, parent):
        LINE_H = 0.086
        PD_Y = 0.01
        next_y = 0.008 + 0.2

        def refresh_y(n_row=1):
            nonlocal next_y
            curr_y = next_y
            for i in range(n_row):
                next_y += LINE_H + PD_Y
            return curr_y

        # row 1
        label = Label(
            parent, text="ICET Student Survey", font=("calibri", 20, "italic", "bold")
        )
        label.place(relx=0.25, rely=0.008, relwidth=0.94, relheight=0.2)

        # row 2
        frame = Frame(parent)
        frame.place(relx=0.03, rely=refresh_y(), relwidth=0.94, relheight=LINE_H)
        label = Label(frame, text="Full name: ")
        entry = Entry(frame, textvariable=self.name)
        label.place(relx=0.0167, rely=PD_Y, relwidth=0.30, relheight=0.98)
        entry.place(relx=0.35, rely=PD_Y, relwidth=0.50, relheight=0.98)

        # row 3-4
        frame = Frame(parent)
        frame.place(relx=0.03, rely=refresh_y(2), relwidth=0.94, relheight=LINE_H * 2)
        label = Label(frame, text="Residency: ")
        radio1 = Radiobutton(
            frame, text="Domestic", variable=self.residency, value="dom"
        )
        radio2 = Radiobutton(
            frame, text="International", variable=self.residency, value="intl"
        )
        label.place(relx=0.0167, rely=PD_Y, relwidth=0.30, relheight=0.98 / 2)
        radio1.place(relx=0.35, rely=PD_Y, relwidth=0.30, relheight=0.98 / 2)
        radio2.place(relx=0.35, rely=PD_Y + 0.5, relwidth=0.30, relheight=0.98 / 2)

        # row 5
        frame = Frame(parent)
        frame.place(relx=0.03, rely=refresh_y(), relwidth=0.94, relheight=LINE_H)
        label = Label(frame, text="Program: ")
        combo = Combobox(frame, values=self.programs, textvariable=self.program)
        label.place(relx=0.0167, rely=PD_Y, relwidth=0.30, relheight=0.98)
        combo.place(relx=0.35, rely=PD_Y, relwidth=0.50, relheight=0.98)

        # row 6-8
        frame = Frame(parent)
        frame.place(relx=0.03, rely=refresh_y(3), relwidth=0.94, relheight=LINE_H * 3)
        label = Label(frame, text="Courses: ")
        check1 = Checkbutton(
            frame,
            text="Programming I",
            variable=self.course1,
            onvalue="COMP100",
            offvalue="",
        )
        check2 = Checkbutton(
            frame,
            text="Web Page Design",
            variable=self.course2,
            onvalue="COMP213",
            offvalue="",
        )
        check3 = Checkbutton(
            frame,
            text="Software Engineering",
            variable=self.course3,
            onvalue="COMP120",
            offvalue="",
        )
        label.place(relx=0.0167, rely=PD_Y, relwidth=0.30, relheight=0.98 / 3)
        check1.place(relx=0.35, rely=PD_Y, relwidth=0.50, relheight=0.98 / 3)
        check2.place(relx=0.35, rely=PD_Y + 1 / 3, relwidth=0.30, relheight=0.98 / 3)
        check3.place(relx=0.35, rely=PD_Y + 2 / 3, relwidth=0.30, relheight=0.98 / 3)

        # row 9
        frame = Frame(parent)
        frame.place(relx=0.03, rely=refresh_y(), relwidth=0.94, relheight=LINE_H)
        resetbtn = Button(frame, text="Reset", command=self.init_ui)
        okbtn = Button(frame, text="Ok", command=self.submit)
        exitbtn = Button(frame, text="Exit", command=parent.quit)
        resetbtn.place(relx=0.0167, rely=PD_Y, relwidth=0.30, relheight=0.98)
        okbtn.place(relx=0.0167 + 0.3, rely=PD_Y, relwidth=0.30, relheight=0.98)
        exitbtn.place(relx=0.0167 + 0.6, rely=PD_Y, relwidth=0.30, relheight=0.98)

    def submit(self):
        message = (
            "Name: "
            + self.name.get()
            + "\nResidency: "
            + self.residency.get()
            + "\nProgram: "
            + self.program.get()
            + "\nCourses: "
        )
        for var in [self.course1, self.course2, self.course3]:
            if var.get():
                message += "\n  -"
                message += var.get()
        messagebox.showinfo("Student Info", message)


app = SurveyGUI()
app.mainloop()
