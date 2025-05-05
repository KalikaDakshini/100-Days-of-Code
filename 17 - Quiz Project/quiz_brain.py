"""
Brain of the Quiz

Classes:
    QuizBrain
"""

import random
from question_model import Question


class QuizBrain:
    """Brains of the Quiz"""

    def __init__(self, data: list[dict]) -> None:
        self.question_list: list[Question] = [
            Question(entry["text"], entry["answer"]) for entry in data
        ]
        self.ques_id = 0
        self.score = 0
        random.shuffle(self.question_list)

    def ask_question(self) -> bool:
        """Ask user a question"""
        # Ask Question
        question = self.get_question()
        if question is None:
            print("You've aced the test. Congrats :D")
            return False

        statement = f"Q.{self.ques_id} {question}"
        while True:
            try:
                # Parse input and evaluate response
                response = input(statement).lower()
                if response in ("true", "false"):
                    return self.evaluate_question(question, response)
                # Invalid input
                raise ValueError
            except ValueError:
                print("Invalid Input, Try gain")

    def evaluate_question(self, ques: Question, resp: str) -> bool:
        """Evaluate the question"""
        if ques.evaluate(resp):
            self.score += 1
            print(f"You've got it right. Your current score is {self.score}\n")
            return True

        print(f"You've got it wrong. Your final score is {self.score}\n")
        return False

    def get_question(self) -> Question | None:
        """
        Return a random question from the list of questions

        If all questions are solved, return None
        """
        if self.ques_id == len(self.question_list):
            return None

        question = self.question_list[self.ques_id]
        self.ques_id += 1
        return question

    def get_score(self) -> int:
        """Return the quiz score"""
        return self.score

    def __str__(self) -> str:
        return "Brains of this operation :D"
