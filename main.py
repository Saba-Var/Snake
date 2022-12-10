from scroeboard import Scoreboard
from game_screen import screen
from snake import Snake
from food import Food
import time

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")

while snake.game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        snake.game_is_on = False
        score.game_over()

    if snake.snake_head.distance(food) < 15:
        food.generate_location()
        score.increase_score()

screen.exitonclick()
