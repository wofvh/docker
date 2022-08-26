class GradeService(object):
    def __init__(self,name,) -> None:
        pass
    
    


class Grade(object):
    def __init__(self,name,kor,eng,meth) :
        self.name = name
        self.kor = kor
        self.eng = eng
        self.meth = meth
        self.avg = 0.0
    
    def set_avgvalue(self):
        self.avg = (self.kor + self.eng + self.meth) / 3
        
        
        
        
    def get_avgvalue(self):
        return self.avg
        
        
        

