from icecream import ic
import pandas as pd
import numpy as np
import string
import random

class PandasQuiz(object):
    def __init__(self) -> None:
        pass
    def quiz_01(self) -> None:
        df1 = pd.DataFrame.from_dict(
            {'1':[1, 3 ,5],'2':[2, 4, 6]}, orient= 'index',
            columns=['a','b','c']
        )
        ic(df1)
    
    def quiz_02(self):
        df2 = pd.DataFrame.from_dict(
            [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],index=range(1,5),
            columns=['a','b','c',])
        ic(df2)