from PIL import Image, ImageDraw

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



def Left_index(points):
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convexHull(points, n):
    if n < 3:
        return
    l = Left_index(points)
    hull = []
    p = l
    q = 0
    while (True):
        hull.append(p)
        q = (p + 1) % n
        for i in range(n):
            if (orientation(points[p],
                            points[i], points[q]) == 2):
                q = i
        p = q
        if (p == l):
            break

    def lst_with_hull():
        lst = []
        for i in hull:
            lst.append(points[i].x )
            lst.append(540 - points[i].y)
        return lst
    lst_with_hull()

    f = open('dataset.txt', 'r')
    data = f.readlines()
    xy = []
    for i in data:
        k,j  = i.split(" ")
        xy.append(int(j))
        xy.append(540 - int(k))
    f.close()

    canvas = Image.new("RGB", (960, 540), (255, 255, 255))
    d = ImageDraw.Draw(canvas)
    d.point(lst_with_hull(), fill=(255, 0, 0))
    d.point(xy, fill=0)
    d.line(lst_with_hull(), fill=(0, 0, 255), width=1 )
    canvas.show()
    canvas.save("pictureHull.png")


f = open('dataset.txt', 'r')
data = f.readlines()
f.close()
points = []
for i in range(len(data)):
    data[i] = data[i].split()
    points.append(Point(int(data[i][1]), int(data[i][0])))

convexHull(points, len(points))



