from dataclasses import dataclass
import icecream as ic
@dataclass
class Context:
    path: str
    fname: str
    train: object
    test: object
    id: str
    label: str
    model: object
    
    
    @property
    def path(self) -> str: return self._path

    @property
    def fname(self) -> str: return self._fname

    @property
    def train(self) -> object: return self._train

    @property
    def test(self) -> object: return self._test

    @property
    def id(self) -> str: return self._id

    @property
    def label(self) -> str: return self._label
    
    @property
    def model(self) -> object: return self._model

    @path.setter
    def path(self, path): self._path = path

    @fname.setter
    def fname(self, fname): self._fname = fname

    @train.setter
    def train(self, train): self._train = train

    @test.setter
    def test(self, test): self._test = test

    @id.setter
    def id(self, id): self._id = id

    @label.setter
    def label(self, label): self._label = label
    
    @model.setter
    def model(self, model): self._model = model
    
    @staticmethod
    def show_spec(param):
        ic(param.shape) #(715, 9) #train_set과 열 값이 '1'차이 나는 건 count를 제외했기 때문이다.예측 단계에서 값을 대입
        ic(param.columns)
        ic(param.info()) #null은 누락된 값이라고 하고 "결측치"라고도 한다.
        ic(param.describe()) 