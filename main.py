from game_screen import screen
from snake import Snake
import time

snake = Snake()

while snake.game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()
