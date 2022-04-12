x = 0
y = 0
mode = "vpravo"
made = "vverh"
def setup():
  size(600,400)
  frameRate(2)
def draw():
  global x,mode,y,made
  background(0)
  ellipse(x,y,40,40)
  push()
  if mode == "vpravo":
      x = x + 20
  if mode == "vlevo":
      x = x - 20
  if x >= 600-20:
      mode = "vlevo"
  if x <= 20:
      mode = "vpravo"
  pop()
  push()
  if made == "vverh":
      y = y + 10
  if made == "vniz":
      y = y - 10
  if y >= 400-20:
      made = "vniz"
  if y <= 20:
      made = "vverh"
  pop()
