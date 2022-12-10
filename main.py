from game_screen import screen
from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for starting_position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(starting_position)

screen.exitonclick()
