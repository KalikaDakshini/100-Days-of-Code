"""Race Master"""

import turtle as t
import random


class RaceTurtle(t.Turtle):
    """Turtle object used for racing"""

    def __init__(self, name: str, *args) -> None:
        super().__init__(*args)
        self.name = name
        self.color(name)
        self.shape("turtle")
        self.speed("normal")
        self.penup()

    def __str__(self) -> str:
        return self.name.capitalize()


class RaceMaster:
    """Controls the race"""

    def __init__(self, racers: list[str]) -> None:
        self.racer_list = [RaceTurtle(racer) for racer in racers[:6]]
        self.screen = t.Screen()
        self.screen.setup(800, 500)
        self.winner = None
        self.race_finished = False
        self.racer_positions = [
            (-350, -60),
            (-350, -120),
            (-350, -180),
            (-350, 60),
            (-350, 120),
            (-350, 180),
        ]

    def begin_race(self):
        """Assign racers to their positions and start race"""
        # Assign racers to their positions
        for racer, pos in zip(self.racer_list, self.racer_positions):
            racer.goto(pos)
        # Start race
        while not self.race_finished:
            for racer in self.racer_list:
                racer.fd(random.randint(10, 20))
                if racer.pos()[0] > 350:
                    self.winner = racer
                    self.race_finished = True
                    break
        self.screen.exitonclick()
        return

    def announce(self):
        """Announce the winner"""
        print(f"{self.winner} won. Congrats")
