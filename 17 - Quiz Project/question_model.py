"""
Module holding the Question class

Classes:
    Question
"""


class Question:
    """Class to model the Question in a Quiz"""

    def __init__(self, question: str, answer: str) -> None:
        self.statement = question
        self.answer = answer.lower()

    def evaluate(self, response: str):
        """Evaluate the answer"""
        return self.answer == response

    def __str__(self) -> str:
        return f"{self.statement} (True or False)?: "
