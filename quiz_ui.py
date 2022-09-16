from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x530")

        # Display Title
        self.display_title()

        # Creating a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()


        self.user_answer = StringVar()

        #El radio de los bootenes
        self.opts = self.radio_buttons()
        self.display_options()

        #Para mostrar si esta bien o mal
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)

        # Sigueinte y quitar o salird el juego
        self.buttons()

        # Mainloop lo importante
        self.window.mainloop()

    def display_title(self):


        # Title
        title = Label(self.window, text="iQuiz Application",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        # lugar del tittle
        title.place(x=0, y=2)

    def display_question(self):
       #mostrar la pregunta

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        #crear los espacios

        # opciones options
        choice_list = []

        # posicion de la rpimera
        y_pos = 220

        # añadir opciones
        while len(choice_list) < 4:


            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))

            ##botones
            choice_list.append(radio_btn)

            # ubicando
            radio_btn.place(x=200, y=y_pos)

            # incremento la ubicacion para q no se suporpognan
            y_pos += 40

        # return the radio buttons
        return choice_list

    def display_options(self):
        #mostrar las 4 opciones

        val = 0

        #Quitar las respuestas
        self.user_answer.set(None)


        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):


        #mira si esta correcto
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oops! \n'
                                     f'The right answer is: {self.quiz.current_question.correct_answer}')

        if self.quiz.has_more_questions():

            self.display_question()
            self.display_options()
        else:
            #el default del socre o la puntuacion al finalizar
            self.display_result()

            # destroys la ventana para mostrar el socre
            self.window.destroy()

    def buttons(self):



        # next Question
        next_button = Button(self.window, text="Next", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))

        # palcing the button  on the screen
        next_button.place(x=350, y=460)

        # El boton  QUIT
        quit_button = Button(self.window, text="Quit", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

      #UBICANDO
        quit_button.place(x=700, y=50)

    def display_result(self):
        #mostrar resultado
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

       #porcentaje
        result = f"Score: {score_percent}%"

       #mostrar el resultado :)
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")