import turtle
import colorsys

# Assignments:
#
# 1. Re-implement main.py to use iteration. 
# (HINT: Use the get_rgb_color function, the colors will be not 
# quite the same but close enough for this assignment.)
#
# 2. Further enhance the program to use a nested loop 
# and produce a 2-dimensional color picker letting you 
# see each of the 6 colors with 6 levels of saturation.

def get_rgb_color(i, j=8):
  # do not worry about the next line
  return colorsys.hsv_to_rgb(i / 6, j / 10, 1)


scrn = turtle.getscreen()
trtl = turtle.Turtle()

trtl.color("red")
trtl.dot(20)
trtl.forward(20)

trtl.color("orange")
trtl.dot(20)
trtl.forward(20)

trtl.color("yellow")
trtl.dot(20)
trtl.forward(20)

trtl.color("green")
trtl.dot(20)
trtl.forward(20)

trtl.color("blue")
trtl.dot(20)
trtl.forward(20)

trtl.color("purple")
trtl.dot(20)
trtl.forward(20)

turtle.mainloop()
