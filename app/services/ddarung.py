from app.models.ddarung import DDarung
import pandas as pd

class DDarungService:
    
    ddarung = DDarung()
    
    def preprocess(self,path,train,test) -> object:
        model = self.ddarung
        this = model.context
        this.train = model.from_csv(path,train)
        this.test = model.from_csv(path,test)
        this.id = this.test['id']
        return this
    
    def submit(self,path,train,test):
        this = self.preprocess(path, train, test)
        print('### DF### 구조보기')
        print(this.train.head())