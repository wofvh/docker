from icecream import ic
import pandas as pd
import numpy as np
import string
import random

class PandasQuiz(object):
    def __init__(self) -> None:
        pass
    def quiz_01(self) -> None:
        df = pd.DataFrame.from_dict(
            {'1':[1, 3 ,5],'2':[2, 4, 6]}, orient= 'index',
            columns=['a','b','c']
        )
        ic(df)
    def quiz_02(self) :
        df = pd.DataFrame([[1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [10,11,12]], index=range(1,5), columns=['A','B','C'])
        ic(df)
        
    def quiz_03(self):
        df = pd.DataFrame(np.random.randint(10, 100, size=(2,3)))
        ic(df)
    def id(self):
        return["".join([random.choice(string.ascii_letters)
                        for i in range(5)]) for i in range(10)]
    def score(self):
        return np.random.randint(0,100,(10,4))
    
    def quiz_04(self):
        df = pd.DataFrame(
            self.score(),
            index=self.id(),
            columns=['국어','영어','수학','사회']
        )
        ic(df)
        return df
    
    def quiz_05(self,subject):
        scores = self.quiz_04()
        scores.loc[:,subject]
    
    # def quiz_05(self,subject):
    #     self.subject = subject
    #     df5 = pd.DataFrame(self.score(),
    #                        index = self.id(),
    #                        columns=['국어', '영어', '수학', '사회'])[f'{self.subject}']
    #     ic(df5)
    
    def quiz_06(self, id) :
        print(f'{id}의 성적출력') # 당연히 id 가 일치할리 없음. 형식적으로 출력함
        scores = self.quiz_04()
        ic(scores.iloc[[0],:])
        
    # def quiz_06(self):
    #     df6 = pd.DataFrame(self.score(),
    #                        index= self.id(),
    #                        columns=['국어','영어','수학','사회'])
    #     ic(df6.iloc[[0]])
     
    def quiz_07(self) :
        scores = self.quiz_04()
        scores['총점'] = scores.sum(axis=1)
        ls = scores.sum().tolist()
        scores.loc['과목총점']= ls
        ic(scores)
        
        
        
                   
    # def quiz_07(self):
    #     random_num = np.random.randint(0,101,(10,5))
    #     df7 = pd.DataFrame(random_num,index = self.id(),
    #                        columns=['국어','영어','수학','사회','과학'])
    #     df7['총점'] = df7['국어'] + df7['영어'] + df7['수학']+df7['사회'] \
    #         + df7['과학']
    #     df7.loc['과목총점']=df7.sum(axis=0)
    #     ic(df7)
