from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.directions = {"right": 0, "up": 90, "left": 180, "down": 270, }
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.game_is_on = True
        self.segments_list = []
        self.travel_distance = 20
        self.create_snake()
        self.snake_head = self.segments_list[0]
        self.snake_head.color("red")

    def create_snake(self):
        for starting_position in self.starting_positions:
            self.add_segment(starting_position)

    def reset(self):
        for segment in self.segments_list:
            segment.goto(2000, 2000)
        self.segments_list.clear()
        self.create_snake()
        self.snake_head = self.segments_list[0]
        self.snake_head.color("red")

    def add_segment(self, starting_position):
        segment = Turtle("square")
        segment.penup()
        segment.color("green")
        segment.goto(starting_position)
        self.segments_list.append(segment)

    def extend(self):
        self.add_segment(self.segments_list[-1].position())

    def change_heading(self, heading, opposite_heading):
        if self.snake_head.heading() != opposite_heading:
            self.snake_head.setheading(heading)

    def up(self):
        self.change_heading(self.directions["up"], self.directions["down"])

    def right(self):
        self.change_heading(self.directions["right"], self.directions["left"])

    def down(self):
        self.change_heading(self.directions["down"], self.directions["up"])

    def left(self):
        self.change_heading(self.directions["left"], self.directions["right"])

    def move(self):
        for i in range(len(self.segments_list) - 1, 0, -1):
            prev_segment = self.segments_list[i - 1]
            new_x = prev_segment.xcor()
            new_y = prev_segment.ycor()
            self.segments_list[i].goto(new_x, new_y)
        self.snake_head.forward(self.travel_distance)
