from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.game_is_on = True
        self.segments_list = []
        self.travel_distance = 20
        self.create_snake()
        self.first_segment = self.segments_list[0]

    def create_snake(self):
        for starting_position in self.starting_positions:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(starting_position)
            self.segments_list.append(segment)

    def move(self):
        for i in range(len(self.segments_list) - 1, 0, -1):
            prev_segment = self.segments_list[i - 1]
            new_x = prev_segment.xcor()
            new_y = prev_segment.ycor()
            self.segments_list[i].goto(new_x, new_y)
        self.first_segment.forward(self.travel_distance)
