"""Draw a hirst dot painting"""

import turtle as t
from turtle import Turtle, Screen
import random


def random_colour():
    """Return a tuple of random RGB"""
    colours = [
        (150, 75, 49),
        (223, 201, 135),
        (52, 93, 124),
        (172, 154, 40),
        (140, 30, 19),
        (133, 163, 185),
        (198, 91, 71),
        (46, 122, 86),
        (72, 43, 35),
        (145, 178, 148),
        (13, 99, 71),
    ]

    return random.choice(colours)


def draw_circle(talia: Turtle, radius: int, colour):
    """Draw a circle and fill it"""
    # Set colour
    talia.color(colour)
    # Draw and fill the circle
    talia.pendown()
    talia.dot(radius)
    talia.penup()


def hirst_painting(talia: Turtle, side: int = 10):
    """Draw a grid of circles"""

    radius = 25
    shift = 2.5 * radius

    talia.speed("fastest")
    talia.pensize(3)
    talia.hideturtle()
    talia.teleport(-300, 300)

    # Draw circles
    for _ in range(side):
        for _ in range(side):
            # Draw a circle and fill it
            draw_circle(talia, radius, random_colour())
            # Move to next circle
            talia.fd(shift)
        # Move to the next row
        talia.back(shift * side)
        talia.setheading(270)
        talia.fd(shift)
        talia.setheading(0)


if __name__ == "__main__":
    t = Turtle()
    S = Screen()
    S.colormode(255)
    S.screensize(1000, 1000)

    hirst_painting(t)
    S.exitonclick()
