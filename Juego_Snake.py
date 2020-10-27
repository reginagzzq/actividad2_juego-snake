#A00827434 Ernesto García González
#A00827107 Regina González Quijano
from turtle import *
from random import randrange
from freegames import square, vector
import random

#la posición de la comida, la serpiente y la dirección se indica con vectores.
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#función que le da valores al vector aim que indica la dirección
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

#función que indica los límites de la ventana del juego y si la serpiente está dentro de la ventana.
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
#función que indica los límites de la ventana del juego y si la comida está dentro de la ventana.
def inside(food):
    "Return True if food inside boundaries."
    return -200 < food.x < 190 and -200 < food.y < 190

#funcino recursiva que controla el movimiento de la serpiente y la comida. Tambien incluye el proceso de la serpiente "comiendo".
def move():
    "Move snake forward one segment."
    val=[-1,0,0,0,0,0,0,0,0,0,0,0,1]
    head = snake[-1].copy()
    food.x= random.choice(val)*10+food.x
    food.y= random.choice(val)*10+food.y
    head.move(aim)
    
    if not inside(food):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10


    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()