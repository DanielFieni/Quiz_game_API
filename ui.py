from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label_score.grid(column=1, row=0)

        self.canvas = Canvas(width=320, height=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, font=("Arial", 20, "italic"), fill="black", text="hdasjkhdas")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.is_true_button)
        self.true_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.is_false_button)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.finish_quiz():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You finished the quiz\nFinish score: {self.quiz.score}/{len(self.quiz.question_list)}") 
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.label_score.config(text="")

    def is_true_button(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)
    
    def is_false_button(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)