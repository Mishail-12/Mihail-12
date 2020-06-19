class  Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_w(self):
        return self.w
    
    def get_h(self):
        return self.h
    
    def intersection(self, other, new):
        if self.y + self.h >= other.y and self.x + self.w >= other.x:
            if other.y + other.h > self.y and other.x + other.w > self.x:
                new.x = sorted(self.x, self.x + self.w, self.y, 
                               self.y + self.h)[2] - sorted(self.x, self.x + self.w, self.y, 
                               self.y + self.h)[1]
        else:    