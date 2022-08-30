from app.models.ddarung import DDarung

class DDarungService:
    ddarung = DDarung()
    
    def preprocess(self,path,train,test) -> object:
        model = self.ddarung
        this = model.context
        this.train = model.from_csv(path,train)
        this.test = model.from_csv(path,test)
    
    def submit(self,path,train,test):
        ddarung = DDarung()
        ddarung.hook(path,train,test)