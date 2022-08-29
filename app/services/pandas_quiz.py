import random
from icecream import ic
import pandas as pd
import numpy as np
import string

class PandasQuiz(object):
    
    def quiz_01(self) -> None :
        df = pd.DataFrame.from_dict(
             {'1': [ 1 , 3 , 5,],'2': [2 , 4 , 6]},
             orient='index',
             columns = ['a','b','c'])
        ic(df)
        
    def quiz_02(self) -> None :
        df1 = pd.DataFrame.from_dict(
             {'1': [ 1 , 2 , 3,],'2':[ 4, 5 , 6],'3': [ 7, 8 , 9],'4': [10, 11 , 12]}, 
             orient='index',
             columns = ['a','b','c'])
        ic(df1)
    
    def quiz_03(self):
        df2= pd.DataFrame(np.random.randint(10,101,size=(2,3)))
        ic(df2)
        
        
    def id1(self):
        return [ "".join([random.choice(string.ascii_lowercase) 
                          for i in range(5)]) for i in range(10)]
    def score1(self):
        return np.random.randint(0,101,(10, 4))
    
    def quiz_04(self) :
        df3 = pd.DataFrame(
            self.score1(), 
            index=self.id1(), 
            columns=['국어', '영어', '수학', '사회'])
        ic(df3) 
        
        
    def quiz_05(self):
        df4 = pd.DataFrame(
            self.score(),
            self.id(),
            columns=['국어'])
        ic(df4)    
        
    def id(self):
        return [ "".join([random.choice(string.ascii_lowercase) 
                          for i in range(1)]) for i in range(10)]
    
    def score(self):
        return np.random.randint(0,101(10,1))
        
    
    
        
        
    ''' 
        # # Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성. 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
        # # ic| self.id(): 'HKKHc'
        # # ic| self.score(): 2
        
        # '''
        #         # Q5-1 국어 점수만 출력    
        #                      hVoGW    93            
        #                      QkpKK    25
        #                      oDmky    82
        #                      qdTeX    51
        #                      XGzWk    34
        #                      PAwgj    85
        #                      vnTmB    28
        #                      wuxIm    58
        #                      AOQFG    32
        #                      jHChe    59
        #                      Name: 국어, dtype: int64
        # '''    
        
        

    def id(self):
        rand_str = ''
        for i in range(5):
            rand_str += random.choice(string.ascii_letters)
        return rand_str
    
    def score(self):
        return random.sample(range(0,100), 4)

    def quiz_04(self):
        ic(self.id())
        ic(self.score())
        df4 = pd.DataFrame.from_dict({self.id():self.score()}, orient='index', columns=['국어', '영어', '수학', '사회'])
        for i in range(8):
            df4 = pd.concat([df4,pd.DataFrame.from_dict({self.id():self.score()}, orient='index', columns=['국어', '영어', '수학', '사회'])],axis=0)
        
        ic(df4)
        
    

