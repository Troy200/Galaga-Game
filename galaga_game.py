import pgzrun


HEIGHT= 700
WIDTH = 1200

bugs=[]

bullets = []



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


Points=0






def draw():
    screen.fill("light blue")
    Galaga.draw()
    for b in bugs:
        b.draw()
    Bullet.draw()
    for b in bullets:
        b.draw()
    screen.draw.text(str(Points),(580,480))

   
        


def update():
    if keyboard.left:
        Galaga.x=Galaga.x-15
        if Galaga.x<20:
            Galaga.x=20
    if keyboard.right:
        Galaga.x=Galaga.x+15
        if Galaga.x>1180:
            Galaga.x=1180
    if keyboard.space:
        nbullet = Actor("bullet")
        nbullet.x = Galaga.x
        nbullet.y = Galaga.y
        bullets.append(nbullet)

    for bul in bullets():
        bul.y -= 10
        if bul.y < 0:
            bullets.remove(bul)
        else:
            for bug in bugs():
                if bul.colliderect(bug):
                    bugs.remove(bug)
                    bullets.remove(bul)
                    Points += 10



    

pgzrun.go()

