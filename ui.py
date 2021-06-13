from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, obj_quizes):
        # Window
        self.window = Tk()
        self.window.title("Quiz Time")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        # Canves
        global Canvas1, Quiz
        Canvas1 = self.canves = Canvas(height=250, width=300)
        Quiz = self.canves.create_text(250/2, 300/2,
                                width= 200,
                                font=("Arial", 15, "italic"),

                                text = obj_quizes.next_question(),
                                fill=THEME_COLOR)

        self.canves.grid(row=1,column=0,columnspan=2, pady=50)


        # Label
        global Label111
        Label111 = self.label = Label(text=f"Score: {obj_quizes.score}", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        # Buttons
        def pressed_yes():
            obj_quizes.check_answer("True")
            check_babe()

        def pressed_no():
            obj_quizes.check_answer("False")
            check_babe()

        def check_babe():
            if obj_quizes.true_false:
                make_green()

            else:
                make_red()
            self.window.after(1000, func=call_question)

        def call_question():
            self.window.config(bg=THEME_COLOR)
            if obj_quizes.still_has_questions():
                Canvas1.itemconfig(Quiz, text=f"{obj_quizes.next_question()}")
                Label111.config(text=f"Score: {obj_quizes.score}")
            else:
                Canvas1.itemconfig(Quiz, text="well played babe")
                self.yes.config(state="disabled")
                self.no.config(state="disabled")

        def make_red():
            self.window.config(bg="red")

        def make_green():
            self.window.config(bg="green")

        self.image_yes = PhotoImage(file="true.png")
        self.yes = Button(image=self.image_yes, command=pressed_yes)
        self.yes.grid(row=2, column=0)
        self.image_no = PhotoImage(file="false.png")
        self.no = Button(image=self.image_no, command=pressed_no)
        self.no.grid(row=2, column=1)



        self.window.mainloop()