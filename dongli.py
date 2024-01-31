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
        self.container = Frame(self)
        self.container["relief"] = "ridge"
        self.container.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.create_variables()
        self.init_ui()
        self.create_ui(self.container)
        self.container.bind("<Configure>", self.on_window_resize)

    def create_styles(self):
        # create style instance
        style = Style()
        # configure global
        style.theme_use("clam")
        style.configure(".", background="#FFF3CF", foreground="black")
        # configure buttons
        style.configure("TButton", background="#637A9F", foreground="white")
        style.map(
            "TButton",
            foreground=[("active", "!disabled", "black")],
            background=[("active", "#E8C872")],
        )
        # configure fonts
        self.font_size = 10
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=self.font_size)

    def on_window_resize(self, event):
        # calculate corresponding font size when resizing window
        area = self.container.winfo_width() * self.container.winfo_height()
        self.font_size = int(10 * (area / (480 * 360)) ** 0.5)
        # configure font size for all elements dynamically
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=self.font_size)
        self.title_font = tkFont.Font(
            size=self.font_size * 2,
            family="Helvetica",
            weight="bold",
            slant="italic",
        )
        self.text_font = tkFont.Font(size=self.font_size)
        self.title_label.configure(font=self.title_font)
        self.name_entry.configure(font=self.text_font)
        self.combo_prog.configure(font=self.text_font)

    def create_variables(self):
        # create variables for data
        self.name = StringVar()
        self.residency = StringVar()
        self.program = StringVar()

        self.course1 = StringVar()
        self.course2 = StringVar()
        self.course3 = StringVar()

        self.programs = ["AI", "Gaming", "Health", "Software"]
        self.courses = [self.course1, self.course2, self.course3]

    def init_ui(self):
        # set default value to variables
        self.name.set("Dongli Liu")
        self.residency.set("dom")
        self.program.set("AI")
        for course in self.courses:
            course.set("")

    def create_ui(self, parent):
        # create const and vars to handle layout
        LINE_H = 0.086
        PD_Y = 0.01
        next_y = 0.008 + 0.2

        def refresh_y(n_row=1):
            # fetch current y location and update next y
            nonlocal next_y
            curr_y = next_y
            for i in range(n_row):
                next_y += LINE_H + PD_Y
            return curr_y

        # row 1
        label = Label(
            parent,
            text="ICET Student Survey",
            font=20,
        )
        label.place(relx=0.25, rely=0.008, relwidth=0.6, relheight=0.2)
        self.title_label = label

        # row 2
        frame = Frame(parent)
        frame.place(relx=0.03, rely=refresh_y(), relwidth=0.94, relheight=LINE_H)
        label = Label(frame, text="Full name: ")
        entry = Entry(frame, textvariable=self.name)
        self.name_entry = entry
        label.place(relx=0.1, rely=PD_Y, relwidth=0.30, relheight=0.98)
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
        label.place(relx=0.1, rely=PD_Y, relwidth=0.30, relheight=0.98 / 2)
        radio1.place(relx=0.35, rely=PD_Y, relwidth=0.30, relheight=0.98 / 2)
        radio2.place(relx=0.35, rely=PD_Y + 0.5, relwidth=0.30, relheight=0.98 / 2)

        # row 5
        frame = Frame(parent)
        frame.place(relx=0.03, rely=refresh_y(), relwidth=0.94, relheight=LINE_H)
        label = Label(frame, text="Program: ")
        combo = Combobox(frame, values=self.programs, textvariable=self.program)
        self.combo_prog = combo
        label.place(relx=0.1, rely=PD_Y, relwidth=0.30, relheight=0.98)
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
        label.place(relx=0.1, rely=PD_Y, relwidth=0.30, relheight=0.98 / 3)
        check1.place(relx=0.35, rely=PD_Y, relwidth=0.50, relheight=0.98 / 3)
        check2.place(relx=0.35, rely=PD_Y + 1 / 3, relwidth=0.50, relheight=0.98 / 3)
        check3.place(relx=0.35, rely=PD_Y + 2 / 3, relwidth=0.50, relheight=0.98 / 3)

        # row 9
        frame = Frame(parent)
        frame.place(relx=0.03, rely=refresh_y(), relwidth=0.94, relheight=LINE_H)
        resetbtn = Button(frame, text="Reset", command=self.init_ui, style="TButton")
        okbtn = Button(frame, text="Ok", command=self.submit, style="TButton")
        exitbtn = Button(frame, text="Exit", command=parent.quit, style="TButton")
        resetbtn.place(relx=0.1, rely=PD_Y, relwidth=0.23, relheight=0.98)
        okbtn.place(relx=0.1 + 0.26, rely=PD_Y, relwidth=0.23, relheight=0.98)
        exitbtn.place(relx=0.1 + 0.52, rely=PD_Y, relwidth=0.23, relheight=0.98)

    # function handle clicking ok
    def submit(self):
        # build message
        message = (
            "Name: "
            + self.name.get()
            + "\nResidency: "
            + self.residency.get()
            + "\nProgram: "
            + self.program.get()
            + "\nCourses: "
        )
        for var in self.courses:
            if var.get():
                message += "\n  -"
                message += var.get()
        # show message
        messagebox.showinfo("Student Info", message)


if __name__ == "__main__":
    app = SurveyGUI()
    app.mainloop()
