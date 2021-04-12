import turtle                                                
import math                            
import random    

#設定畫面                                     
wn = turtle.Screen()                                
wn.bgcolor("black")                                
wn.title("Space invaders")

#畫框線
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    border_pen.hideturtle()

#設定初始分數為零
score = 0

#畫分數版
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = f"Score: {score}"
score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
score_pen.hideturtle()

#創立玩家
player= turtle.Turtle()
player.color("blue")
player.shape("square")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#玩家跟敵人的移動速度
playerspeed = 15
enemyspeed = 2

#設定敵人數量
number_of_enemies = 5

#創一個空的串列儲存敵人
enemies = []

#加入敵人
for i in range(number_of_enemies):
    # 加入敵人
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("square")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

#創玩家的子彈
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

#設定子彈的速度
bulletspeed = 70

#確認是否發射子彈
bulletstate = "ready"

#玩家左右移動
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x =- 280
    player.setx(x)
    print(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    print(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        return True
    else:
        return False

#連結鍵盤
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#主程式
while True:

    for enemy in enemies:
        #移動敵人
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1

        #確認是否子彈碰到敵人
        if isCollision(bullet, enemy):
            #重設子彈
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -340)
            #重設敵人
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #更新分數
            score += 10
            scorestring = f"Score: {score}"
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
        
        #確認是否玩家碰到敵人
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #移動子彈
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    #確認子彈超過螢幕頂端
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

while True:
    wn.update()