x = 0
def setup():
  size(600,400)
  colorMode(HSB,100,100,100)
def draw():
  global x
  translate(400,200)
  rotate(radians(x))
  stroke(random(0,100),100,100)
  line(0,0,50,50)
  x = x + 1
