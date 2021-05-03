import turtle
import colorsys

def get_rgb_color(i, j=8):
  return colorsys.hsv_to_rgb(i / 6, j / 10, 1)

scrn = turtle.getscreen()
trtl = turtle.Turtle()

i = 0 # start of loop
while i < 6: # end of loop condition
  trtl.setpos(i * 20, 0)
  trtl.color(get_rgb_color(i))
  trtl.dot(20)
  i = i + 1 


turtle.mainloop()