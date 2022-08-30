from app.utils.context import Context
from app.models.titanic import Titanic
from sklearn.svm import SVC
import pandas as pd


class TitanicService(object):

    titanic = Titanic()

    def preprocess(self, path, train, test) -> object:
        model = self.titanic
        this = model.context
        this.train = model.from_csv(path, train)
        this.test = model.from_csv(path, test)
        this.id = this.test['PassengerId']
        # print(f'트레인 드랍 전 컬럼 : {this.train.columns}')
        this = model.drop_feature(this, 'Cabin')
        this = model.drop_feature(this, 'Ticket')
        # print(f'트레인 드랍 후 컬럼 : {this.train.columns}')
        this = model.embarked_nominal(this)
        this = model.title_nominal(this)
        this = model.drop_feature(this, 'Name')
        this = model.drop_feature(this, 'PassengerId')
        this = model.age_ordinal(this)
        this = model.sex_nominal(this)
        this = model.fareBand_nominal(this)
        this = model.drop_feature(this, 'Fare')
        print(f'전처리 마감 후 컬럼 : {this.train.columns}')
        print(f'train 널의 수량 : {this.train.isnull().sum()}')
        print(f'test 널의 수량 : {this.test.isnull().sum()}')
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        print(f'결정트리 활용한 검증 정확도 {model.accuracy_by_dtree(this)}')
        print(f'랜덤포레스트 활용한 검증 정확도 {model.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 활용한 검증 정확도 {model.accuracy_by_nb(this)}')
        print(f'KNN 활용한 검증 정확도 {model.accuracy_by_knn(this)}')
        print(f'SVM 활용한 검증 정확도 {model.accuracy_by_svm(this)}')
        return this

    def submit(self, path, train, test):
        print(f'path : {path}')
        this = self.preprocess(path, train, test)
        
        clf = SVC()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame(
            {'PassengerId' : this.id, 'Survived': prediction}
        ).to_csv(f'{path}submission.csv', index_label=False)
