class Grade(object):
    def __init__(self,name, kor,eng,math) :
        self.name = name 
        self.kor = kor
        self.eng = eng
        self.math = math
        self.avg = 0.0
        
    def set_avg(self):
        self.avg = (self.kor + self.eng + self.math)/3
    
    def get_avg(self):
        return self.avg
    
        
    