import turtle as tu
import time as t
import random as r

points = 0
animations_counter = 10

screen = tu.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Selfmade Game")
screen.tracer(0)

score = tu.Turtle()
score.penup()
score.hideturtle()
score.speed(0)

head = tu.Turtle()
head.shape("square")
head.shapesize(stretch_wid=1, stretch_len=1, outline=1.0)
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = tu.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(r.randint(-14 , 14)* 20, r.randint(-14 , 13) * 20)

game_over = False

animation_floating = tu.Turtle()
animation_floating.speed(0)
animation_floating.color("green")
animation_floating.penup()
animation_floating.hideturtle()

animations_counter = 0
anim_x = 0
anim_y = 0

def move_snake(head):
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

def going_up():
    if head.direction != "down":
        head.direction = "up"

def going_down():
    if head.direction != "up":
        head.direction = "down"

def going_left():
    if head.direction != "right":
        head.direction = "left"

def going_right():
    if head.direction != "left":
        head.direction = "right"


def check_collision(head, segments):
    for segment in segments:
        if head.distance(segment) < 20:
            return True
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        return True
    return False

def text(title, score_position, color="white"):
    score.color(color)
    score.goto(score_position)
    score.write(title, align="center", font=("Courier", 24, "normal"))
    return score

def restart_game(head):
    head.goto(0, 0)
    head.direction = "stop"
    global points, game_over
    points = 0
    game_over = False
    food.goto(r.randint(-14 , 14)* 20, r.randint(-14 , 13) * 20)
    text("Game Restarted!", (0, 0))
    t.sleep(1)
    score.clear() 
        
def start_floating_animation(x, y):
    global animations_counter, anim_x, anim_y
    anim_x = x
    anim_y = y
    animations_counter = 10  # Animation läuft für 10 Frames

def update_floating_animation():
    global animations_counter, anim_y
    if animations_counter >= 0:
        animation_floating.clear()
    
        if animations_counter > 0:
            anim_y += 4  # Bewegt den Text pro Frame um 4 Pixel nach oben
            animation_floating.goto(anim_x, anim_y)
            animation_floating.write("+1 Point!", align="center", font=("Courier", 14, "bold"))
            animations_counter -= 1

segments = []
screen.listen()
screen.onkeypress(lambda: going_up(), "w")
screen.onkeypress(lambda: going_down(), "s")
screen.onkeypress(lambda: going_left(), "a")
screen.onkeypress(lambda: going_right(), "d")
screen.onkeypress(lambda: restart_game(head), "r")

while True:
    screen.update()
    if not game_over:
        if head.distance(food) < 20:
            points += 1
            start_floating_animation(food.xcor(), food.ycor())
            score.clear()
            text(f"Score: {points}", (0, 260))
            food.goto(r.randint(-14 , 14)* 20, r.randint(-14 , 13) * 20)
            new_segment = tu.Turtle()
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            segments[0].goto(head.xcor(), head.ycor())
        move_snake(head)
        update_floating_animation()
        if check_collision(head, segments):
            head.goto(1000, 1000)
            head.direction = "stop"
            food.goto(1000, 1000)
            food.clear()
            for segment in segments:
                segment.goto(1000, 1000)  # Move segments off-screen
                text("Press 'R' to Restart", (0, -30))
            segments.clear()
            game_over = True
        
    t.sleep(0.1)  # Add a small delay to control the game speed