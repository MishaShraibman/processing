x = 0
y = 0
mode = "vpravo"
made = "vverh"
b = 0.1
a = 0.1
def setup():
  size(600,400)
  frameRate(220)
def draw():
  global x,mode,y,made,b,a
  background(0)
  ellipse(x,y,40,40)
  push()
  if mode == "vpravo":
      x = x + b
  if mode == "vlevo":
      x = x - b
  if x >= 600-20:
      mode = "vlevo"
      a = random(0,0.5)
      b = random(0,0.5)
  if x <= 20:
      a = random(0,0.5)
      b = random(0,0.5)
      mode = "vpravo"
      
  pop()
  push()
  if made == "vverh":
      y = y + a
  if made == "vniz":
      y = y - a
  if y >= 400-20:
      a = random(0,0.5)
      b = random(0,0.5)
      made = "vniz"
  if y <= 20:
      a = random(0,0.5)
      b = random(0,0.5)
      made = "vverh"
  pop()
