from fnmatch import fnmatchcase
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
from app.utils.context import Context

class DDarung:
    
    context = Context()
    
    def __init__(self) -> None:
        self.train_set_clean = None
        self.model = None
        self.x_test = None
        self.y_test = None
        
    def from_csv(self,path, fname):
        this = self.context
        this.path = path
        this.fname = fname
        return pd.read_csv(this.path+this.fname)
    
    def fillna_median(self, this):
        train = this.train
        test = this.test
        this.train = train.fillna(train.median())
        this.test = test.fillna(test.median())
        return this
    
    def fillna_interpolate(self, this):
        train = this.train
        test = this.test
        this.train = train.interpolate()
        this.test = test.interpolate()
        return this
        
    def fillna_mean(self, this):
        train = this.train
        test = this.test
        this.train = train.fillna(train.mean())
        this.test = test.fillna(test.mean())
        return this
    
    def drop_na(self, this):
        train = this.train
        test = this.test
        this.train = train.dropna()
        this.test = test.dropna()
        return this

    def outliers(self, data_out):
        quartile_1, q2 , quartile_3 = np.percentile(data_out,
                                                [25,50,75]) # percentile 백분위
        print("1사분위 : ",quartile_1) # 25% 위치인수를 기점으로 사이에 값을 구함
        print("q2 : ",q2) # 50% median과 동일 
        print("3사분위 : ",quartile_3) # 75% 위치인수를 기점으로 사이에 값을 구함
        iqr =quartile_3-quartile_1  # 75% -25%
        print("iqr :" ,iqr)
        lower_bound = quartile_1 - (iqr * 1.5)
        upper_bound = quartile_3 + (iqr * 1.5)
        return np.where((data_out>upper_bound)|
                        (data_out<lower_bound))
    '''
    Index(['hour', 'hour_bef_temperature', 'hour_bef_precipitation',
               'hour_bef_windspeed', 'hour_bef_humidity', 'hour_bef_visibility',
               'hour_bef_ozone', 'hour_bef_pm10', 'hour_bef_pm2.5', 'count'],  
    '''
    def make_stereotype(self, this):
        train = this.train 
        hour_bef_precipitation_out_index= self.outliers(train['hour_bef_precipitation'])[0]
        hour_bef_windspeed_out_index= self.outliers(train['hour_bef_windspeed'])[0]
        hour_bef_humidity_out_index= self.outliers(train['hour_bef_humidity'])[0]
        hour_bef_visibility_out_index= self.outliers(train['hour_bef_visibility'])[0]
        hour_bef_ozone_out_index= self.outliers(train['hour_bef_ozone'])[0]
        hour_bef_pm10_out_index= self.outliers(train['hour_bef_visibility'])[0]
        hour_bef_pm25_out_index= self.outliers(train['hour_bef_pm2.5'])[0]
        # print(train_set2.loc[hour_bef_precipitation_out_index,'hour_bef_precipitation'])
        lead_outlier_index = np.concatenate((hour_bef_precipitation_out_index,
                                            hour_bef_windspeed_out_index,
                                            hour_bef_humidity_out_index,
                                            hour_bef_visibility_out_index,
                                            hour_bef_ozone_out_index,
                                            hour_bef_pm10_out_index,
                                            hour_bef_pm25_out_index),axis=None)
        print(len(lead_outlier_index)) #161개 
        print(lead_outlier_index)
        lead_not_outlier_index = []
        for i in train.index:
            if i not in lead_outlier_index :
                lead_not_outlier_index.append(i)
        train = train.loc[lead_not_outlier_index]      
        train = train.reset_index(drop=True)
        this.train = train
        return this
    
    def extract_label_in_train(self, this):
        train = this.train
        this.label = train['count']
        this.train = train.drop(['count'],axis=1) 
        # Context.show_spec(this.train)
        return this

    def learning(self, this):
        x = np.array(this.train)
        y = np.array(this.label)
        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, train_size=0.7, random_state=1234)

        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)

        model = BaggingRegressor(DecisionTreeRegressor(),
                                n_estimators=100,#해당 모델을 100번 훈련한다.
                                n_jobs=-1,
                                random_state=123
                                )
        # Bagging 할 때는 스케일링이 무조건 필요하다.
        # Bagging(Bootstrap Aggregating)
        # 한가지 모델을 여러번 훈련한다.대표적인 Ensemble 모데 랜덤포레스트
        #3. 훈련
        model.fit(x_train,y_train)
        #4. 평가, 예측
        print('model.score :',model.score(x_test,y_test))
        return this

        #=================  결측치 median 처리  =============  
        # tree-0.5338291078101032
        # forest-0.7827754490472193
        # xgb-0.7864238734420762   
        #=================  결측치 interpolate 처리  =============  
        # tree-0.65829171863489
        # forest-0.7879504683704567
        # xgb-0.7914603072315469
        #=================  결측치 mean 처리  =============  
        # tree-0.6058261668039286
        # forest-0.7857045058880551
        # xgb-0.7967861479060181

        ######Bagging 후 r2 Df
        # model.score : 0.7877370090310412

        ######Bagging 후 r2 model xgb
        # model.score : 0.8107202578169292

        ######Bagging 후 r2 model rf
        # model.score : 0.7753138544272746