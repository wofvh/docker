import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService

def print_menu():
    print("0. 전체종료프로그램 종료") 
    print("1. 계산기 프로그램")
    meun = input("메뉴를 선택하세요:")
    return meun
     
def main():
    print_menu()
    calculatorService = CalculatorService()
    while 1 :
        meun = print_menu()
        if meun == '0':
            print("프로그램을 종료합니다.")
            break
                
    if __name__ == '__main__':
        main()