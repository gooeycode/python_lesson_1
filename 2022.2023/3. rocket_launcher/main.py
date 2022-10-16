#!/bin/python3

# Import library code
from p5 import *
from random import randint

# Setup global variables
screen_size = 400
rocket_y = screen_size

# The draw_rocket function goes here
def draw_rocket():
  global rocket_y
  rocket_y -= 1
  image(rocket, width/2, rocket_y, 64, 64)


# The draw_background function goes here
def draw_background():
  background(0)
  image(purple_planet, width/2, height, 300, 300)

def setup():
  # Setup your animation here
  size(screen_size, screen_size)
  image_mode(CENTER)
  global purple_planet, rocket
  purple_planet = load_image('purple_planet.png')
  rocket = load_image('rocket.png')
  
def draw():
  # Things to do in every frame
  draw_background()
  draw_rocket()
  
    
run()