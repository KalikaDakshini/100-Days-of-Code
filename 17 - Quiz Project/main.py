"""Main file of the program."""

from quiz_brain import QuizBrain
from data import question_data

if __name__ == "__main__":
    quiz_master = QuizBrain(question_data)
    while quiz_master.ask_question():
        pass
