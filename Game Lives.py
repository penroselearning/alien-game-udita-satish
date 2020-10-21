HEIGHT = 500
WIDTH = 500

LIVES = 3
speed = 1
score = 0
alien_status = ""
game_status = 0

alien=Actor("alien")
alien.pos = 10,250

def draw():
    global game_status
    if game_status == 0:
        screen.blit("space1", (0, 0))
        screen.draw.text("Press enter to start the game",center=(WIDTH /2, HEIGHT / 2),color="white",gcolor="pink",fontname="dephiana",fontsize=36)
        #screen.blit("space1", (0, 0))
    if LIVES == 0:
        game_status = 2

    if game_status == 1:
        screen.blit("space1", (0, 0))
        alien.draw()
        screen.draw.text("Click me",(150,65),fontname="krinkes",color="white",gcolor="#c2b8ff",fontsize=65)
        screen.draw.text(f"Score:{str(score)}",(350,450),color="white",gcolor="yellow",fontname="blob")
        screen.draw.text(f"Remaining Lives:{str(LIVES)}",(35,450), color="white",gcolor="orange",fontname="dephiana",owidth=1,ocolor="black")
    if game_status == 2:
        global alien_status
        screen.clear()
        alien_status=""
        screen.blit("space2",(0,0))
        screen.draw.text("Game over",center=(WIDTH / 2, HEIGHT / 2),color="#ffb8ca",gcolor="#f78b1e",fontname="dephiana",fontsize=55)
        screen.draw.text("©UditaSatish",(350,450),color="#0affff",fontsize=25)
    if alien_status == "Hit":
        screen.draw.text("OUCH!",(250,350),color="#ff7081")
    if alien_status == "Missed":
        screen.draw.text("MISSED!",(250,350),color="#ff7081")







def update():
    global speed,LIVES,score,alien_status,game_status
    if game_status==0:
        if keyboard.RETURN:
            game_status=1
    if game_status == 1:
        alien.left+=speed
    if alien.left>WIDTH:
        alien.left=15
    if LIVES <= 0:
        LIVES = 0
    if speed <=1:
        speed=1
    if score <=0:
        score=0

def on_mouse_down(pos,button):
    global score,LIVES,speed,alien_status,game_status
    if alien.collidepoint(pos):
        score += 1
        speed += 1
        alien_status = "Hit"
        sounds.splat.play()
        alien.image = 'alien_hurt'
        clock.schedule_unique(set_alien_normal, 0.5)
        if button == mouse.LEFT and alien.collidepoint(pos):
            print("Ouch!! Left click hurts")
        elif button == mouse.RIGHT and alien.collidepoint(pos):
            print("Ouch!! Right Click hurts more")
        else:
            print("Ah ha! You missed me!")


    else:
        score-=1
        speed-=1
        LIVES-=1
        alien_status="Missed"
        sounds.eep.play()

def set_alien_normal():
    alien.image="alien"







