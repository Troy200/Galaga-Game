import pgzrun
import time

HEIGHT= 700
WIDTH = 1200

bugs=[]




Galaga=Actor("galaga")
Galaga.y=(655)
Galaga.x=(585)

Bullet=Actor("bullet")
Bullet.x=Galaga.x
Bullet.y=Galaga.y



for i in range(5):

    Bug=Actor("bug")
    Bug.x=(585+40*i)
    Bug.y=(30)
    bugs.append(Bug)









def draw():
    screen.fill("light blue")
    Galaga.draw()
    for b in bugs:
        b.draw()
    Bullet.draw()
        


def update():
    if keyboard.left:
        Galaga.x=Galaga.x-15
        if Galaga.x<20:
            Galaga.x=20
    if keyboard.right:
        Galaga.x=Galaga.x+15
        if Galaga.x>1180:
            Galaga.x=1180
    

pgzrun.go()

