"""Snake object for the game"""

from turtle import Turtle


class Snake:
    """Snek"""

    def __init__(self, length: int = 5) -> None:
        self._len = length
        start_positions = [(-20 * i, 0) for i in range(self._len)]
        # Initiate and move the turtle segments to their positions
        self.segments = [Turtle() for _ in range(self._len)]
        for idx, segment in enumerate(self.segments):
            segment.shape("square")
            segment.penup()
            segment.color("white")
            x, y = start_positions[idx]
            segment.goto(x, y)

        self._head = self.segments[0]

    def move(self):
        """Move the snake"""
        # Move the snake in an iterative fashion where the nth segment
        # goes to (n-1)th position
        for i in range(self._len - 1, 0, -1):
            next_seg = self.segments[i - 1]
            x, y = next_seg.xcor(), next_seg.ycor()
            self.segments[i].goto(x, y)
        self._head.fd(20)

    def turn(self, angle: int):
        """Turn the snake in the direction"""
        if abs(self._head.heading() - angle) != 180:
            self._head.setheading(angle)
