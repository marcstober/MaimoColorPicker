import turtle
import colorsys

# copy this function for now
def get_rgb_color(i, j=.8):
  return colorsys.hsv_to_rgb(i / 6, 1 - j * .9 / 6, 1)

scrn = turtle.getscreen()
trtl = turtle.Turtle()

i = 0 # start of loop
while i < 6: # end of loop condition
  j = 0 # start of nested loop
  while j < 6:
    trtl.setpos(i * 20, j * 20)
    trtl.color(get_rgb_color(i, j))
    trtl.dot(20)
    j += 1 # note!  
  i += 1 # `i++` in C-style languages, like, of course, C++

turtle.mainloop()