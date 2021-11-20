from tkinter import *
from tkinter import messagebox as mb

import json
# class to define the components of the GUI
class Quiz:

    def __init__(self):
        # set question number to 0
        self.q_no = 0
        self.q_nos = -1
        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_notice()
        self.display_question()

        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected = IntVar()

        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts = self.radio_buttons()

        # display options for the current question
        self.display_options()

        # displays the button for next and exit.
        self.buttons()

        # no of questions
        self.data_size = len(question)

        # keep a counter of correct answers
        self.correct = 0
    def display_result(self):
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):

        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            # if the option is correct it return true
            return True

    def next_btn(self):
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1

        # checks if the q_no size is equal to the data size
        if self.q_no == self.data_size:

            # if it is correct then it displays the score
            self.display_result()

            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()


    def previous_btn(self):
        # Moves to previous Question by decrementing the q_no counter
        self.q_no -= 1

        # checks if the q_no size is equal to first question
        if self.q_no == self.q_nos:
            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()

    def save_btn(self):
        # Check if the answer is correct
        if self.check_ans(self.q_no):
            # if the answer is correct it increments the correct by 1
            self.correct += 1

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=250, y=380)

        previous_button = Button(gui, text="Previous", command=self.previous_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        previous_button.place(x=250, y=320)

        save_button = Button(gui, text="Save", command=self.save_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        save_button.place(x=450, y=320)

        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=10, bg="blue", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=450, y=380)


    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # This method shows the current Question on the screen
    def display_question(self):

        # setting the Question properties
        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')

        # placing the option on the screen
        q_no.place(x=70, y=100)

    # This method is used to Display Title
    def display_title(self):

        # The title to be shown
        title = Label(gui, text="Question Bank",
                      width=50, bg="yellow", fg="red", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)


    def display_notice(self):

        # The notice to be shown at the end
        title = Label(gui, text="Please save the answer before going to another Question",
                      width=50, bg="white", fg="black", font=("ariel", 10, "bold"))

        # place of the notice
        title.place(x=220, y=450)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        # adding the options to the list
        while len(q_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 16))

            # adding the button to the list
            q_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=100, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return q_list

# Create a GUI Window
gui = Tk()

# set the size of the GUI Window
gui.geometry("850x500")

# set the title of the Window
gui.title("Python Quiz")

# get the data from the json file
with open('data.json.txt') as f:
    data = json.load(f)

# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

# create an object of the Quiz Class.
quiz = Quiz()

# Start the GUI
gui.mainloop()

# END OF THE PROGRAM
