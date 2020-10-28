#A00827434 Ernesto García González
#A00827107 Regina González Quijano

from turtle import *
from random import randrange
from freegames import square, vector
import random

#La posición de la comida, la serpiente y la dirección se indican con vectores.
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colores  = ["blue","orange","purple","pink","yellow"]

#Función que le da valores al vector aim que indica la dirección
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

#Función que indica los límites de la ventana del juego y si la serpiente está dentro de la ventana.
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Función que indica los límites de la ventana del juego y si la comida está dentro de la ventana.
def inside(food):
    "Return True if food inside boundaries."
    return -200 < food.x < 190 and -200 < food.y < 190

#Función recursiva que controla el movimiento de la serpiente y la comida. Tambien incluye el proceso de la serpiente "comiendo".
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
    
    #Función para el cuerpo de la serpiente. El color random está definido por color_s
    for body in snake:
        square(body.x, body.y, 9, color_s)
    
    #Características de la comida. El color random de la comida está definido por color_f
    square(food.x, food.y, 9, color_f)
    update()
    ontimer(move, 100)

#Main-code
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# variable para el color de la serpiente usando la lista de colores y la acción random
color_s = random.choice(colores)
# variable para el color de la comida usando la lista de colores y la acción random
color_f = random.choice(colores)

move()
done()