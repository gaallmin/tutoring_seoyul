'''
객체지향 언어
쉽게 말해서: 파이썬으로 객체(물체)를 만든다는 것
즉 우리가 프로그래밍으로 실제 존재하는 물체를 재현하는 것

지금 주위를 보면 물체로 둘러싸여 있여있을 것이다
=> 물체는 어떻게 이뤄져있을까

예를 들어 자동차는 엔진이 있고, 부속물체가 있고, 색깔도 있고 등 여러가지
특징이 있다. 이런 것들을 물체의 속성이라고 한다,
속성은 영어로는 attribute, 즉 객체가 무엇인지 또는 무엇을 가지고 있는지를 나타냄

attribute = is/ has ex) name, age, height

또 자동차는 동작 면에서 보면 빠르게 갈 수도 있고 멈출 수도 있다. 이런
것 들을 method라고 하면,
우리는 물체를 attribute와 method를 이용해서 설명할 수 있다.

methods = actions ex) eat, sleep, enjoy, study


클래스를 만드는 것을 이런 attribute와 method를 미리 적어둔 설계도를
만든다고 생각해보자
이런 설계도는 다른 파일에 있어도 되고 같은 파일 안에 있어도 된다


 self refers to the object that is

using this method
'''
#클래스를 만드는데 규칙 : 클래스 이름은 대문자로
class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")

from Car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.drive()
car_2.stop()





# flash card exp
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.lower()


class FlashcardQuiz:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)

    def start_quiz(self):
        if not self.flashcards:
            print("No flashcards in the quiz. Add some flashcards first.")
            return

        random.shuffle(self.flashcards)
        score = 0

        for i, flashcard in enumerate(self.flashcards, 1):
            print(f"Question {i}: {flashcard.question}")
            user_answer = input("Your answer: ")

            if flashcard.check_answer(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect! The correct answer was: {flashcard.answer}\n")

        print(f"Quiz finished! Your final score is {score} out of {len(self.flashcards)}.")


# Example usage
quiz = FlashcardQuiz()
quiz.add_flashcard("What is the capital of France?", "Paris")
quiz.add_flashcard("What is the smallest planet in our solar system?", "Mercury")
quiz.add_flashcard("Who wrote 'Romeo and Juliet'?", "William Shakespeare")

quiz.start_quiz()



# tinker

import tkinter as tk
from tkinter import messagebox
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.lower()


class FlashcardQuiz:
    def __init__(self):
        self.flashcards = []
        self.current_card = None
        self.score = 0
        self.index = 0

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)

    def start_quiz(self):
        if not self.flashcards:
            messagebox.showwarning("Warning", "No flashcards in the quiz. Add some flashcards first.")
            return

        random.shuffle(self.flashcards)
        self.score = 0
        self.index = 0
        self.next_card()

    def next_card(self):
        if self.index < len(self.flashcards):
            self.current_card = self.flashcards[self.index]
            self.index += 1
            return True
        else:
            return False

    def check_current_answer(self, user_answer):
        if self.current_card and self.current_card.check_answer(user_answer):
            self.score += 1
            return True
        return False


class FlashcardQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz")
        self.quiz = FlashcardQuiz()

        # Create GUI components
        self.question_label = tk.Label(root, text="Question", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Question", command=self.load_next_card)
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=20)

        # Add some sample flashcards
        self.quiz.add_flashcard("What is the capital of France?", "Paris")
        self.quiz.add_flashcard("What is the smallest planet in our solar system?", "Mercury")
        self.quiz.add_flashcard("Who wrote 'Romeo and Juliet'?", "William Shakespeare")

        # Start the quiz
        self.quiz.start_quiz()
        self.load_next_card()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        if self.quiz.check_current_answer(user_answer):
            self.result_label.config(text="Correct!", fg="green")
        else:
            correct_answer = self.quiz.current_card.answer
            self.result_label.config(text=f"Incorrect! The correct answer was: {correct_answer}", fg="red")

        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.answer_entry.delete(0, tk.END)

    def load_next_card(self):
        if self.quiz.next_card():
            self.question_label.config(text=self.quiz.current_card.question)
            self.result_label.config(text="")
        else:
            self.question_label.config(text="Quiz Finished!")
            self.result_label.config(text=f"Your final score is {self.quiz.score} out of {len(self.quiz.flashcards)}.")
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)


# Running the application
root = tk.Tk()
app = FlashcardQuizApp(root)
root.mainloop()
