"""Main Game Object"""

from turtle import Screen
from snake import Snake
from time import sleep


class SnakeGame:
    """Main game object"""

    def __init__(self, width: int = 900, height: int = 900) -> None:
        # Initialize the screen
        self._screen = Screen()
        self._screen.setup(width, height)
        self._screen.bgcolor("black")
        self._screen.title("Snake Game")
        self._screen.tracer(0)
        # Initialize the snake
        self.snek = Snake(5)

    def run(self):
        """Run the game"""
        # Set up events
        self._screen.listen()
        self._screen.onkeypress(lambda: self.snek.turn(90), "Up")
        self._screen.onkeypress(lambda: self.snek.turn(0), "Right")
        self._screen.onkeypress(lambda: self.snek.turn(180), "Left")
        self._screen.onkeypress(lambda: self.snek.turn(270), "Down")
        while True:
            sleep(0.1)
            self.snek.move()
            self._screen.update()


if __name__ == "__main__":
    snake_game = SnakeGame()
    snake_game.run()
