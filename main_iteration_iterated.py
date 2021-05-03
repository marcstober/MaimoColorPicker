import turtle
import colorsys

STEPS = 6
SIZE = 20

# copy this function for now
def get_rgb_color(i, j=.8):
  return colorsys.hsv_to_rgb(i / STEPS, 1 - j * .9 / STEPS, 1)

scrn = turtle.getscreen()
trtl = turtle.Turtle()

offset = STEPS * SIZE / 2

for i in range(STEPS): # end of loop condition
  for j in range(STEPS):
    trtl.setpos(i * SIZE - offset, j * SIZE - offset)
    trtl.color(get_rgb_color(i, j))
    trtl.dot(SIZE)

turtle.mainloop()