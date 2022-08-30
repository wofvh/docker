from cProfile import label
from dataclasses import dataclass
@dataclass  #데코레이터
class Context:
    path: str
    fname: str
    train:object
    test: object
    id:str
    label:str
    
    @property
    def path(self) -> str:return self._path     #<<안에 감취진 파일 (#객터 모양) 
    
    @path.setter
    def path(self, path): self._path = path
    
    @property
    def fname(self) -> str: return self._fname
    
    @fname.setter
    def fname(self, fname) : self._fname = fname
    
    @property
    def train(self) -> object: return self._train
    
    @fname.setter
    def train(self,train) : self._train = train
    
    @property
    def test(self) -> object: return self._test
    
    @test.setter
    def test(self,test) : self._test = test
    
    @property
    def id(self) -> str: return self._id
    
    @id.setter
    def id(self,id) : self._id = id
    
    @property
    def label(self) -> str: return self._label
    
    @label.setter
    def label(self,label): self._label = label