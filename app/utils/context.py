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
    def path(self) -> str:return self._path   #<<안에 감취진 파일 (#객터 모양) 
    
    @path.setter
    def path(self, path): self._path = path
    