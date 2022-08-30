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
        this = model.fillna_median(this)
        this = model.fillna_interpolate(this)
        this = model.fillna_mean(this)
        this = model.drop_na(this)
        this = model.make_stereotype(this)
        return this
        
    
    def submit(self, path, train, test):
        this = self.preprocess(path, train, test)
        Context.show_spec(this.train)
        '''
        count  = 0
        pd.Dataframe({'id': this.id, 'count':count})
        '''