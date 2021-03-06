def setup():
    size(640, 360, P3D)
    noStroke()
    fill(204)

def draw():
    background(0)
    lights()

    if(mousePressed):
        fov = PI/3.0
        cameraZ = (height/2.0) / tan(fov/2.0);
        perspective(fov, float(width)/float(height), cameraZ/2.0, cameraZ*2.0)
    else:
        ortho(0, width, 0, height)

    translate(width/2, height/2, 0)
    rotateX(-PI/6)
    rotateY(PI/3)
    box(160)
