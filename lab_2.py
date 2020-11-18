from PIL import Image, ImageDraw

f = open('dataset.txt', 'r')
data = f.readlines()
xy = []
for i in data:
    x,y = i.split(" ")
    xy.append(int(y))
    xy.append(540 - int(x))
f.close()

canvas = Image.new("RGB", (960, 540), (255, 255, 255))
d = ImageDraw.Draw(canvas)
d.point(xy, fill=0)
canvas.show()
canvas.save("IMAGE", "PNG")

