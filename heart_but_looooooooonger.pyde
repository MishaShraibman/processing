x = 0
x = 0
def setup():
  size(600,400)
  colorMode(HSB,100,100,100)
def draw():
  global x
  translate(300,200)
  rotate(radians(45))
  push()
  translate(20,-100)
  fill(100,100,100)
  stroke(100,100,100)
  rect(0,0,100,100)
  pop()
  push()
  translate(70,-109)
  fill(100,100,100)
  stroke(100,100,100)
  ellipse(0,0,102,102)
  pop()
  push()
  translate(10,-50)
  fill(100,100,100)
  stroke(100,100,100)
  ellipse(0,0,102,102)
  pop()
