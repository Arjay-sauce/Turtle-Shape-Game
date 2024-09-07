# Instructions :
# - Use the arrow keys to move the player turtle.
# - The objective is to catch the red target circle.
# - Every time you catch the target, a new enemy will appear.
# - Avoid all the enemies if you collide with any enemy it's game over.
# - Catch 10 targets to win the game.

import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Shape Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Create the target shape
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.goto(random.randint(-280, 280), random.randint(-280, 280))

# Create an initial enemy
enemies = []

def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape("triangle")
    enemy.color("blue")
    enemy.penup()
    enemy.speed(1)
    enemy.goto(random.randint(-280, 280), random.randint(-280, 280))
    enemies.append(enemy)

# Initialize the score
score = 0

# Create a score display turtle
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Move the player turtle
def move_up():
    y = player.ycor()
    if y < 290:
        player.sety(y + 20)
    check_boundaries()

def move_down():
    y = player.ycor()
    if y > -290:
        player.sety(y - 20)
    check_boundaries()

def move_left():
    x = player.xcor()
    if x > -290:
        player.setx(x - 20)
    check_boundaries()

def move_right():
    x = player.xcor()
    if x < 290:
        player.setx(x + 20)
    check_boundaries()

# Check for collision with the target
def check_collision():
    global score
    if player.distance(target) < 20:
        target.goto(random.randint(-280, 280), random.randint(-280, 280))
        score += 1
        update_score()
        create_enemy()
        if score == 10:
            win_game()

# Check for collision with any enemy
def check_enemy_collision():
    for enemy in enemies:
        if player.distance(enemy) < 20:
            game_over()

# Check if the player moves outside the screen boundaries
def check_boundaries():
    x = player.xcor()
    y = player.ycor()
    if x < -290 or x > 290 or y < -290 or y > 290:
        game_over()

# Update the score display
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Game over function
def game_over():
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write("Game Over!", align="center", font=("Courier", 36, "bold"))
    time.sleep(2)
    turtle.bye()

# Winning the game function
def win_game():
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write("You win!", align="center", font=("Courier", 36, "bold"))
    time.sleep(2)
    turtle.bye()

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Move all enemies slowly
def move_enemies():
    for enemy in enemies:
        x = enemy.xcor() + random.randint(-20, 20)
        y = enemy.ycor() + random.randint(-20, 20)
        if x < -290 or x > 290:
            x = random.randint(-280, 280)
        if y < -290 or y > 290:
            y = random.randint(-280, 280)
        enemy.goto(x, y)

# Main game loop
def main_game_loop():
    while True:
        screen.update()
        check_collision()
        check_enemy_collision()
        move_enemies()
        time.sleep(0.3)

# Start with one enemy
create_enemy()

main_game_loop()

turtle.mainloop()
