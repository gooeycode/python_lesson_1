#!/bin/python3

# Import library code
from p5 import *
from math import *
from random import randint

# The mouse_pressed function goes here
def mouse_pressed():
  
  #points and promt given when mouse is pressed
  if hit_color == outer:
    print('You hit the outer circle, 50 points!')
  elif hit_color == inner:
    print('You hit the inner circle, 200 points!')
  elif hit_color == bulleye:
    print('You hit bullseye, 500 points!')
  else:
    print('You missed! No points!')
  

# The shoot_arrow function goes here
def shoot_arrow():
  global hit_color
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  hit_color = get(arrow_x, arrow_y)
  ellipse(arrow_x, arrow_y , 15, 15)

def setup():
# Setup your game here
  size(400, 400) # width and height
  frame_rate(2)


def draw():
# Things to do in every frame
  global outer, inner, bulleye
  sky = color(92, 205, 206) # Red = 92, Green = 204, Blue = 206
  grass = color(149, 212, 122)
  wood = color(145, 96, 51)
  outer = color(0, 120, 180)
  inner = color(210, 60, 60)
  bulleye = color(220, 200, 0)
  
  no_stroke()

  # set the background grass and sky colours and shapes
  fill(sky)
  rect(0, 0, 400,250)
  fill(grass)
  rect(0, 250, 400, 150)
  
  #set the stand and bullseye colours and shapes
  fill(wood)
  triangle(150, 350, 200, 150, 250, 350)
  fill(outer)
  ellipse(200, 200, 170, 170)
  fill(inner)
  ellipse(200, 200, 110, 110)
  fill(bulleye)
  ellipse(200, 200, 30, 30)
  
  #set arrow colour and call function to shoot arrow
  fill(wood)
  shoot_arrow()
  

  
# Keep this to run your code
run()
