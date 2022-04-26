a = 0
def setup():
    size(600,400)
    background(255)
    
def draw():
    global a
    fill(255)
    ellipse(400,350,100,50)
    if mousePressed == True and a == 1:
        ellipse(mouseX,mouseY,50,50)
    
def mouseClicked():
   global a
   xDif = 400 - mouseX
   yDif = 350 - mouseY
   if sqrt(xDif*xDif + yDif*yDif) < 35:
      if a == 0:
          a = 1
      else:
          a = 0
    
