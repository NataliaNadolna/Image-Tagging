class Coordinates():
    def __init__(self, x: int, y: int, w: int, h: int, size: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.size = size
        self.x1 = int(x*size - w*size/2)
        self.y1 = int(y*size - h*size/2)
        self.x2 = int(x*size + w*size/2)
        self.y2 = int(y*size + h*size/2)

    def __str__(self):
        return f"({self.x1}, {self.y1}), ({self.x2}, {self.y2})"