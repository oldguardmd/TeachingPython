# This was written by ChatGPT with minor edits by me.

import turtle
import math

# Constants
ARM_LENGTH = 100
ROTATION_SPEED = 2  # Adjust the rotation speed as needed

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Rotating Arms")
screen.bgcolor("black")

# Create the first turtle for the first arm
arm1 = turtle.Turtle()
arm1.speed(0)  # Set the turtle's speed to the maximum
arm1.color("white")
arm1.pensize(5)

# Create the second turtle for the second arm
arm2 = turtle.Turtle()
arm2.speed(0)
arm2.color("white")
arm2.pensize(5)

# Main loop
while True:
    arm1.setheading(arm1.heading() + math.radians(ROTATION_SPEED))
    arm2.setheading(arm2.heading() + math.radians(ROTATION_SPEED))

    # Calculate the positions of the ends of the arms
    x1, y1 = arm1.position()
    x2, y2 = x1 + ARM_LENGTH * math.cos(math.radians(arm1.heading())), y1 + ARM_LENGTH * math.sin(math.radians(arm1.heading()))

    # Move the second arm to the end of the first arm
    arm2.setposition(x2, y2)

    # Update the screen
    screen.update()
