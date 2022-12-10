from constants import starting_positions
from game_screen import screen
from turtle import Turtle
import time

segments_list = []

for starting_position in starting_positions:
    segment = Turtle("square")
    segment.penup()
    segment.color("white")
    segment.goto(starting_position)
    segments_list.append(segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    for i in range(len(segments_list) - 1, 0, -1):
        prev_segment = segments_list[i - 1]
        new_x = prev_segment.xcor()
        new_y = prev_segment.ycor()
        segments_list[i].goto(new_x, new_y)

screen.exitonclick()
