from app.utils.context import Context
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
'''
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
'''

class Titanic(object):

    context = Context()

    def from_csv(self, path, fname):
        this = self.context
        this.path = path
        this.fname = fname
        print(f'컨텍스트 경로 : {this.path+this.fname}')
        return pd.read_csv(this.path+this.fname)

    def create_train(self, this):
        return this.train.drop('Survived', axis = 1)

    def create_label(self, this):
        return this.train['Survived']

    def drop_feature(self, this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1)
        return this

    def embarked_nominal(self, this) -> object:
        this.train = this.train.fillna({'Embarked' : 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q' : 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    def fare_ordinal(self, this) -> object:
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels={1, 2, 3, 4}) # FareBand 는 new Feature 가 된다.
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1, 2, 3, 4})
        return this

    def fareBand_nominal(self, this) -> object:
        this.train = this.train.fillna({'FareBand' : 1})
        this.test = this.test.fillna({'FareBand': 1})
        return this

    def title_nominal(self, this) -> object:
        combine = [this.train, this.test] # Title 는 new Feature 가 된다.
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            for dataset in combine:
                dataset['Title'] = dataset['Title'].map(title_mapping)
                dataset['Title'] = dataset['Title'].fillna(0)
            this.train = this.train
            this.test = this.test
        return this

    def sex_nominal(self, this) -> object:
        combine = [this.train, this.test]
        sex_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        this.train = this.train
        this.test = this.test
        return this

    def age_ordinal(self, this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)
        age_title_mapping = {
            0: 'Unknown', 1: 'Baby', 2: 'Child', 3: 'Teenager', 4: 'Student', 5: 'Young Adult', 6: 'Adult', 7: 'Senior'
        }
        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
                train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x] == 'Unknown':
                test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]
        age_mapping = {
            'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
            'Young Adult': 5, 'Adult': 6, 'Senior': 7
        }
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = train
        this.test = test
        return this

    # 머신 러닝
    def create_k_fold(self):
        return KFold(n_splits=10, shuffle=True, random_state=0)

    def accuracy_by_dtree(self, this):
        score = cross_val_score(DecisionTreeClassifier(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10, shuffle=True, random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_rforest(self, this):
        score = cross_val_score(RandomForestClassifier(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10, shuffle=True, random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_nb(self, this):
        score = cross_val_score(GaussianNB(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10, shuffle=True, random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)



    def accuracy_by_knn(self, this):
        score = cross_val_score(KNeighborsClassifier(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10, shuffle=True, random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_svm(self, this):
        score = cross_val_score(SVC(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10, shuffle=True, random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)