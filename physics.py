import math
import random

class Vec2():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def dot(v1,v2):
        return v1.x * v2.x + v1.y * v2.y
    
    def nomalize(v):
        return v / v.norm()
    
    def norm(self):
        return math.sqrt(Vec2.dot(self,self))
    
    def __add__(self, v):
        return Vec2(self.x + v.x, self.y + v.y)
    
    def __neg__(self):
        return Vec2(-self.x,-self.y)
    
    def __sub__(self, v):
        return self + (-v)
    
    def __mul__(self, v):
        if isinstance(v, Vec2):
            return Vec2(self.x * v.x, self.y * v.y)
        return Vec2(self.x * v, self.y * v)
    
    def __rmul__(self, v):
        return self.__mul__(v)
    
    def __truediv__(self, v):
        if isinstance(v, Vec2):
            return Vec2(self.x / v.x, self.y / v.y)
        return Vec2(self.x / v, self.y / v)
    
    def __str__(self):
        return '[ %.4f, %.4f ]' % (self.x, self.y)
    
class object():
    def __init__(self, x, y):
        self.pos = Vec2(x,y)
    