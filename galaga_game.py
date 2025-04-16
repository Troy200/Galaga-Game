import pgzrun


HEIGHT= 700
WIDTH = 1200

bugs=[]
bugs2rem=[]
bullets2rem=[]
bullets = []
directside=1
directupdown=False



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
    if len(bugs)==0:
        screen.draw.text("Gameover",(600,350))

   
        


def update():
    global Points, directside, directupdown
    directupdown=False
    if keyboard.left:
        Galaga.x=Galaga.x-15
        if Galaga.x<20:
            Galaga.x=20
    if keyboard.right:
        Galaga.x=Galaga.x+15
        if Galaga.x>1180:
            Galaga.x=1180
    if keyboard.space:
        nbul = Actor("bullet")
        nbul.x = Galaga.x
        nbul.y = Galaga.y
        bullets.append(nbul)

    for bul in bullets:
        bul.y -= 10
        if bul.y < 0:
            bullets.remove(bul)
        else:
            for bug in bugs:
                if bul.colliderect(bug):
                    bugs2rem.append(bug)
                    bullets2rem.append(bul)
                    Points += 10

    if len(bugs)>0 and ( bugs[0].x<20 or bugs[-1].x>1180):
        directside=directside*-1
        directupdown=True

    for bu in bugs:
        bu.x+=directside*10
        if directupdown==True:
            if bu.y<=700:
                bu.y=bu.y+10

    for i in bugs2rem:
        if i in bugs:
            bugs.remove(i)

    for i in bullets2rem:
        if i in bullets:
            bullets.remove(i)
            
        



    

pgzrun.go()

