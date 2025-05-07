"""Simulate Etch-A-Sketch"""

import turtle as t

if __name__ == "__main__":
    talia = t.Turtle()
    scilia = t.Screen()

    talia.shape("turtle")
    talia.pensize(3)
    talia.color("red")

    scilia.onkeypress(lambda: talia.left(10), "Left")
    scilia.onkeypress(lambda: talia.right(10), "Right")
    scilia.onkeypress(lambda: talia.fd(10), "Up")
    scilia.onkeypress(lambda: talia.back(10), "Down")
    scilia.onkeypress(
        lambda: (talia.ht() if talia.isvisible() else talia.st()), "h"
    )
    scilia.listen()
    scilia.exitonclick()
