from turtle import Turtle, Screen
import random

game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Pick a color: ")
colors = ["pink", "yellow", "blue", "green", "red", "orange"]
y_position = [-100, -60, -20, 20, 60, 100]

all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            game_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The winner is {winning_color}!")
            else:
                print(f"Better luck next time! The winner is {winning_color}!")

        random_movement = random.randint(0, 10)
        turtle.forward(random_movement)


screen.exitonclick()