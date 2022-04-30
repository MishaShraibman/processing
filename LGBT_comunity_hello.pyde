
def setup():
    size(600,400)
    colorMode(HSB,360,100,100)
    background(360,0,100)
    
def draw():
    if keyPressed:
        if key == 'L' or key == 'l' or key == 'Д' or key == 'д':
            background(0,100,100)
        elif key == 'G' or key == 'g' or key == 'П' or key == 'п':
            background(60,100,100)
        elif key == 'B' or key == 'b' or key == 'И' or key == 'и':
            background(120,100,100)
        elif key == 'T' or key == 't' or key == 'Е' or key == 'е':
            background(240,100,100)
    else:
        background(360,0,100)
            
