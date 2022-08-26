import os
import sys
4
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
from app.services.pandas_quiz import PandasQuiz
from app.services.grade import GradeService
from app.services.calculator import CalculatorService
from app.services.user import UserService

def print_menu():
    print("0. 전체종료프로그램 종료") 
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램") #입력받은 아이디와 비번 콘솔에 출력하기
    print('3. 성적표 프로그램')
    print('4. 판다스 퀴즈풀기')
    meun = input("메뉴를 선택하세요:")
    return meun
     
def main():
    
    while 1 :
        meun = print_menu()
        if meun == '0':
            print("프로그램을 종료합니다.")
            break
        elif meun == '1':
            calculatorService = CalculatorService()
            first = int(input("첫번쨰수를 입력하세요:"))
            second = int(input("두번쨰수를 입력하세요:"))
            calculatorService.caluclate(first,second)
        elif meun == "2":
            userService = UserService()
            id = input("아이디를 입력하세요:")
            password = input("비밀번호를 입력하세요:")
            userService.login(id,password)
        elif meun == "3":
            gradeService = GradeService()
            name = input("점수는 :")
            korean = int(input("국어"))
            english = int(input("영어:"))
            math = int(input("수학:"))
            grade = gradeService.get_grade(name,korean,english,math)
            print(f'이름:{name} 학점:{grade}')
      
        elif meun == "4":
            Quiz = PandasQuiz()
            while 1:
                quiz_number = input("퀴즈번호를 입력하세요:")
                if quiz_number == '0':
                    break
                elif quiz_number == '1':
                    Quiz.quiz_01()
                elif quiz_number == '2':
                    Quiz.quiz_02()
                elif quiz_number == '3':
                    Quiz.quiz_03()
                                     
if __name__ == '__main__':
        main()

              
   