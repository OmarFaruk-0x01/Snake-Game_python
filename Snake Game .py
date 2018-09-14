from turtle import *
from time import sleep
from random import randint
win = Screen()
win.title("Snake Game")
win.setup(width=600,height=600)
win.tracer(0)
dela=0.1
#head
head = Turtle()
head.color("#696969")
head.shape("square")
head.penup()
head.speed(0)
head.diraction = "stop"

#food
food = Turtle()
food.color('orange')
food.penup()
food.shape("circle")
food.speed(0)

#scoreing
scr=Turtle()
scr.color("black")
scr.shape("triangle")
scr.penup()
scr.speed(0)
scr.hideturtle()
scr.goto(0,240)
scr.write("Score: 0 Highscore: 0",align="center",font=("arial",10,"bold"))
score=-1
highscore=-1

own=Turtle()
own.color("black")
own.shape("triangle")
own.penup()
own.speed(0)
own.hideturtle()
own.goto(-250,-280)
own.write("Created By OMar ",font=("arial",5,"bold"))
#key press function
def go_up():
	dec = head.diraction
	if dec != "down":
		head.diraction = "up"
def go_down():
	if head.diraction != "up":
		head.diraction = "down"
def go_left():
	if head.diraction != "right":
		head.diraction = "left"
def go_right():
	if head.diraction != "left":
		head.diraction = "right"
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")
# head move function 
def move():
	dec = head.diraction
	if dec == "up":
		head.sety(head.ycor()+10)
	elif dec == "down":
		head.sety(head.ycor()-10)
	elif dec == "left":
		head.setx(head.xcor()-10)
	elif dec == "right":
		head.setx(head.xcor()+10)
#body segment
segment=[]
while True:
	win.update()
	if head.xcor() < -290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() > 290:
		head.goto(0,0)
		head.diraction = "stop"
		for segments in segment:
			segments.goto(5000,5000)
		score=0
		dela=0.1
		scr.clear()
		scr.write(f"Score: {score} Highscore: {highscore}",align="center",font=("arial",10,"bold"))
		segment=[]
	if head.distance(food) < 20:
		food.goto(randint(-290,290),randint(-290,290))
		
		#new body segment
		new_segment = Turtle()
		new_segment.speed(0)
		new_segment.color("#A9A9A9")
		new_segment.shape("square")
		new_segment.penup()
		segment.append(new_segment)
		
		#scoring
		score+=1
		if score > highscore:
			highscore = score
		scr.clear()
		scr.write(f"Score: {score} Highscore: {highscore}",align="center",font=("arial",10,"bold"))
		dela+=0.001
	#add body with head
	for i in range(len(segment)-1,0,-1):
		x,y=segment[i-1].xcor(),segment[i-1].ycor()
		segment[i].goto(x,y)
	if len(segment) > 0:
		segment[0].goto(head.xcor(),head.ycor())
	move()
	#cut body
	for segments in segment:
		if head.distance(segments) < 10:
			head.goto(0,0)
			head.diraction = "stop"
			for i in segment:
				i.goto(500,500)
			score=0
			scr.clear()
			scr.write(f"Score: {score} Highscore: {highscore}",align="center",font=("arial",10,"bold"))
			segment=[]
		dela=0.1
	sleep(dela)
win.mainloop()