class Highwayman:
    def __init__(self, name, sv, k):
        self.name = name
        self.sv = sv
        self.k = k
        self.f = -1
        
    def __str__(self):
        return  '{} {} - {}'.format('Highwayman', self.name, self.sv)
    
    def lie(self):
        self.f += 1
        if self.f % 2 == 0:
            self.k += 1
            return False
        return True
           
    def boast(self):
        return 'Uhaha' * self.k
        
    def change_property(self, property):
        self.sv = property
        
    def __eq__(self, other):
        return
    
    def __ne__(self, other):
        return   
    
    def __lt__(self, other):
        return
    
    def __gt__(self, other):
        return 
    
    def __le__(self, other):
        return    
    
    def __ge__(self, other):
        return        