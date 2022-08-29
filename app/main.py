# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# basedir = os.path.dirname(os.path.abspath(__file__))
# # sys.modules[__name__] = main()
# from app.services.pandas_quiz import PandasQuiz
# from app.services.grade import GradeService
# from app.services.calculator import CalculatorService
# from app.services.user import UserService

# def print_menu():
#     print("0. 전체종료프로그램 종료") 
#     print("1. 계산기 프로그램")
#     print("2. 로그인 프로그램") #입력받은 아이디와 비번 콘솔에 출력하기
#     print('3. 성적표 프로그램')
#     print('4. 판다스 퀴즈풀기')
#     meun = input("메뉴를 선택하세요:")
#     return meun
     
# def main():
    
#     while 1 :
#         meun = print_menu()
#         if meun == '0':
#             print("프로그램을 종료합니다.")
#             break
#         elif meun == '1':
#             calculatorService = CalculatorService()
#             first = int(input("첫번쨰수를 입력하세요:"))
#             second = int(input("두번쨰수를 입력하세요:"))
#             calculatorService.caluclate(first,second)
#         elif meun == "2":
#             userService = UserService()
#             id = input("아이디를 입력하세요:")
#             password = input("비밀번호를 입력하세요:")
#             userService.login(id,password)
#         elif meun == "3":
#             gradeService = GradeService()
#             name = input("점수는 :")
#             korean = int(input("국어"))
#             english = int(input("영어:"))
#             math = int(input("수학:"))
#             grade = gradeService.get_grade(name,korean,english,math)
#             print(f'이름:{name} 학점:{grade}')
      
#         elif meun == "4":
#             Quiz = PandasQuiz()
#             while 1:
#                 quiz_number = input("퀴즈번호를 입력하세요:")
#                 if quiz_number == '0':
#                     break
#                 elif quiz_number == '1':
#                     Quiz.quiz_01()
#                 elif quiz_number == '2':
#                     Quiz.quiz_02()
#                 elif quiz_number == '3':
#                     Quiz.quiz_03()
#                 elif quiz_number == '4':
#                     Quiz.quiz_04()
                                     
# if __name__ == '__main__':
#         main()

              
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
from app.api.endpoints.url import Url
from app.constants.menus import LOGIN, LOGOUT, CALCULATOR, GRADE, \
    QUIZ_1, QUIZ_2, QUIZ_3, QUIZ_4, QUIZ_5

def print_menu():
    print(' ###################')
    print(f'로그인 : {LOGIN}')
    print(f'로그아웃 : {LOGOUT}')
    print(f'계산기 : {CALCULATOR}')
    print(f'성적표 : {GRADE}') 
    print(f'퀴즈 1 : {QUIZ_1}') 
    print(f'퀴즈 2 : {QUIZ_2}')
    print(f'퀴즈 3 : {QUIZ_3}')
    print(f'퀴즈 4 : {QUIZ_4}')
    print(f'퀴즈 4 : {QUIZ_5}')
    # print(f'퀴즈 4 : {QUIZ_6}')
    # print(f'퀴즈 4 : {QUIZ_7}')
    menu = input('메뉴에서 URL을 카피해서 입력하시오\n')
    print(' ###################')
    return menu
    
def main():
    url = Url()
    while 1:
        menu = print_menu()
        if menu == f'{LOGOUT}':
            break
        else : url.router(menu)
                         
            
if __name__ == '__main__' :
    main()