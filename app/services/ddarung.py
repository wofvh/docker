from app.models.ddarung import DDarung
from app.utils.context import Context
import pandas as pd

class DDarungService:
    
    ddarung = DDarung()
    
    def preprocess(self, path, train, test) -> object:
        model = self.ddarung
        this = model.context
        this.train = model.from_csv(path, train)
        this.test = model.from_csv(path, test)
        this.id = this.test['id']
        
        this1 = model.fillna_median(this)
        this2 = model.fillna_interpolate(this) # 가장 우수함
        this3 = model.fillna_mean(this)
        this4 = model.drop_na(this)
        this = model.make_stereotype(this2)
        this = model.extract_label_in_train(this)
        this = model.learning(this)
        return this
        
    
    def submit(self, path, train, test):
        self.preprocess(path, train, test)
        
        '''
        count  = 0
        pd.Dataframe({'id': this.id, 'count':count})
        '''
        