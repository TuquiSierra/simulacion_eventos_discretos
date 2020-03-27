from simpy import Resource

class Person():
    def __init__(self, idx):
        self.idx=idx
        self.partner=None
        self.available=True
        self.childs=0
        self.age=0
        self.couple_check=False
       
class Woman(Person):
    def __init__(self,idx):
        super().__init__(idx)
        self.sex='F'
        self.pregnant=False
        
        
class Man(Person):
    def __init__(self,idx):
        super().__init__(idx)
        self.sex='M'
        
class Couple():
    def __init__(self, p1, p2):
        if p1.sex=='F':
            self.woman=p1
            self.man=p2
        else:
            self.man=p1
            self.woman=p2
    def __eq__(self, value):
        return self.woman==value.woman and self.man==value.man