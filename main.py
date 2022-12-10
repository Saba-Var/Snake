from game_screen import screen
from snake import Snake
import time

snake = Snake()

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

screen.exitonclick()
