import turtle
import os

#screen
win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor('red')
win.title("pongs")
win.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx= 3
ball.dy= 3

#paddle_a_up
def paddle_a_up():
    y = paddle_a.ycor() 
    y += 40      #change y by 20
    paddle_a.sety(y)



#paddle_a_down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40  #change y by 20
    paddle_a. sety(y)

#paddle_b_up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 40      #change y by 20
    paddle_b.sety(y)

#paddle_b_down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40  #change y by 20
    paddle_b. sety(y)




#key bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

#score
score_a = 0
score_b = 0
score = turtle.Turtle()
score.hideturtle()
score.pencolor("white")
score.penup()
score.goto(0,250)
score.write(f"Score A ={score_a}   Score B = {score_b}", font = ("OpenSans", 30, "normal"), align = "center")

#fileA
scorefileA = open("highscoreA.txt","w")

scorefileA.write(str(score_a))


#fileB
scorefileB = open("highscoreB.txt","w")

scorefileB.write(str(score_b))



#main game loop

while True:
    win.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

# top and bottom bounce
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav &")

    elif ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav &")

# left and right 
    
    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1
        os.system("afplay ebounce.wav &")
        score_a += 1
        score.clear()
        score.write(f"Player A = {score_a}  Player B = {score_b}", font = ("OpenSans", 30, "normal"), align = "center" )
        print(score_a)
        scorefileA = open("highscoreA.txt","w+")
        if score_a > int(scorefileA.read()):
            scorefileA.write(str(score_a))
            scorefileA.close()

        
    

    
    elif ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
        os.system("afplay ebounce.wav &")
        score_b += 1
        score.clear()
        score.write(f"Player A = {score_a}  Player B = {score_b}", font = ("OpenSans", 30, "normal"), align = "center" )   
        print(score_b)
        scorefileB = open("highscoreB.txt","w+")
        if score_b > int(scorefileB.read()):
            scorefileB.write(str(score_b))
            scorefileB.close()

        

#border checking for the paddles
    if 250 < paddle_a.ycor() :
        paddle_a.goto(-350,250)
    elif -250 > paddle_a.ycor() : 
        paddle_a.goto(-350,-250) 

    
    if 300 < paddle_b.ycor() + 50 :
        paddle_b.goto(350,250)
    elif -300 > paddle_b.ycor() - 50 : 
        paddle_b.goto(350,-250) 

    
    # paddle and ball collision 
    
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50 :
        ball.setx(-340)
        ball.dx *= -1 
        os.system("afplay bounce.wav &")

    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50 :
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav &")