import pgzrun
import random
WIDTH=600
HEIGHT=600
TITLE="galaxy game"

def draw():
    screen.fill("black")
    i.draw()
    shp.draw()

i=Actor("insect")
shp=Actor("space ship")

i.x=random.randint(50,550)
i.y=20

shp.x=300
shp.y=540



def update():
    global score

    i.y=i.y+2
    if i.y>650:
        i.x=random.randint(50,550)
        i.y=20

    if keyboard.left:
        shp.x=shp.x-2
    if keyboard.right:
        shp.x=shp.x+2


pgzrun.go()