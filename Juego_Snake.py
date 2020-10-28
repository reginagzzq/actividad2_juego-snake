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

#Grupo de colores disponibles que pueden tomar la comida y la serpiente.
colores  = ["blue","orange","purple","pink","yellow","cyan"]

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
    
    #grupo de valores de movimiento que puede tener la comida. Se toma un nímero al azar para moverse en el eje x y el eje y.
    val=[-1,0,0,0,0,0,0,0,0,0,0,0,1]
    food.x= random.choice(val)*10+food.x
    food.y= random.choice(val)*10+food.y
    
    #Función que realiza el movimiento de la serpiente y hace que los cuadros que conforman su cuerpo sigan a "head"
    head = snake[-1].copy()
    head.move(aim)
    
    #Si la comida llega al limite del mapa, se mueve a un lugar aleatorio dentro der este.
    if not inside(food):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    #si la cabeza de la serpiente llega al limite del mapa, se acaba el juego.
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    
    snake.append(head)

    #Al tomar la comida, la serpiente crece y la comida cambia de lugar
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    
    #Elimina el valor del vector que representa la cabeza de la serpiente para poder remplazarlo con el nuevo y simular el movimiento    
    else:
        snake.pop(0)
    
    #Limpia los cuadros resaltados en la pantalla para solamente dejar a la serpiente y a la comida.
    clear()
    
    #Función para el cuerpo de la serpiente. El color random está definido por color_s
    for body in snake:
        square(body.x, body.y, 9, color_s)
    
    #Características de la comida. El color random de la comida está definido por color_f
    square(food.x, food.y, 9, color_f)
    update()
    ontimer(move, 100)

#Main-code
#Se crea la ventana del juego y se inicializa turtle
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

#Teclas que controlan el movimiento de la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# variable para el color de la serpiente usando la lista de colores y la acción random
color_s = random.choice(colores)
colores.remove(color_s)

# variable para el color de la comida usando la lista de colores y la acción random
color_f = random.choice(colores)

move()
done()