from app.models.grade import Grade
class GradeService(object):
    def __init__(self) -> None:
        self.credit = 0
    
    def set_score(self, name, korean, english, math):
        grade = Grade(name, korean, english, math)
        grade.set_avg()
        avg = grade.get_avg()
        
        if avg >= 90:
            self.credit = 'A'
        elif avg >= 80:
            self.credit = 'B'
        elif avg >= 70:
            self.credit = 'C'
        elif avg >= 60:
            self.credit = 'D'
        elif avg >= 50:
            self.credit = 'E'
        else :
            self.credit = 'F'
        
    
    def get_grade(self, name, korean, english, math):
        self.set_score(name, korean, english, math)
        return self.credit
    






