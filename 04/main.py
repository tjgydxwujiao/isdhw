class Ellipse(object):
    def __init__(self,lax,sax):
        self.lax=lax
        self.sax=sax

    def area(self):
        return 3.14*self.lax*self.sax

class Circle(Ellipse):

    def __init__(self,sax):
        self.lax=sax
        self.sax=sax

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Square(Rectangle):

    def __init__(self, width):
        self.width  = width
        self.height = width

def compute_area(shapes):
    total_area= 0
    for i in shapes:
        total_area = add(total_area, i)
    return total_area
