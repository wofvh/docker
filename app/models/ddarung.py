from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor

class DDarung:
    
    def __init__(self) -> None:
        self.train_set = None
        self.test_set = None
        self.train_set_clean = None
        self.model = None
        self.x_test = None
        self.y_test = None
        
    
    def hook(self):
        self.from_csv()
        self.preprocess()
        self.learning()
        self.test()
    
    def from_csv(self):
        #1. 데이터
        path = 'C:\_data\ddarung/' # ".은 현재 폴더"
        train_set = pd.read_csv(path + 'train.csv',
                                )
        test_set = pd.read_csv(path + 'test.csv', #예측에서 쓸거야!!
                            )
        # submission = pd.read_csv(path + 'submission.csv',#예측에서 쓸거야!!
        #                        index_col=0)
                            
        # print(test_set)
        # print(test_set.shape) #(715, 9) #train_set과 열 값이 '1'차이 나는 건 count를 제외했기 때문이다.예측 단계에서 값을 대입

        # print(test_set.columns)
        # print(train_set.info()) #null은 누락된 값이라고 하고 "결측치"라고도 한다.
        # print(train_set.describe()) 
    
    def preprocess(self):
        self.missing_value_process_median()
        self.missing_value_process_interpolate()
        self.missing_value_process_mean()
        self.missing_value_process_drop()
        
    
    def missing_value_process_median(self):

        ###### 결측치 처리 1.median ##### 
        print(train_set.isnull().sum()) #각 컬럼당 결측치의 합계
        train_set = train_set.fillna(train_set.median())
        print(train_set.isnull().sum())
        print(train_set.shape)
        test_set = test_set.fillna(test_set.median())
    def missing_value_process_interpolate(self):
        print(train_set.isnull().sum()) #각 컬럼당 결측치의 합계
        train_set = train_set.interpolate()
        print(train_set.isnull().sum())
        print(train_set.shape)
        test_set = test_set.interpolate()
        
    def missing_value_process_mean(self):
        print(train_set.isnull().sum()) #각 컬럼당 결측치의 합계
        train_set = train_set.fillna(train_set.mean())
        print(train_set.isnull().sum())
        print(train_set.shape)
        test_set = test_set.fillna(test_set.mean())
        
    def missing_value_process_drop(self):
        train_set = self.train_set
        test_set = self.test_set
        print(train_set.isnull().sum()) #각 컬럼당 결측치의 합계
        train_set2 = train_set.dropna()
        print(train_set.isnull().sum())
        print(train_set.shape)
        test_set2 = test_set.dropna()

    def outliers(data_out):
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
    
    def dont_know(self):
        # Index(['hour', 'hour_bef_temperature', 'hour_bef_precipitation',
        #        'hour_bef_windspeed', 'hour_bef_humidity', 'hour_bef_visibility',
        #        'hour_bef_ozone', 'hour_bef_pm10', 'hour_bef_pm2.5', 'count'],  
        train_set = self.train_set  
        hour_bef_precipitation_out_index= self.outliers(train_set['hour_bef_precipitation'])[0]
        hour_bef_windspeed_out_index= self.outliers(train_set['hour_bef_windspeed'])[0]
        hour_bef_humidity_out_index= self.outliers(train_set['hour_bef_humidity'])[0]
        hour_bef_visibility_out_index= self.outliers(train_set['hour_bef_visibility'])[0]
        hour_bef_ozone_out_index= self.outliers(train_set['hour_bef_ozone'])[0]
        hour_bef_pm10_out_index= self.outliers(train_set['hour_bef_visibility'])[0]
        hour_bef_pm25_out_index= self.outliers(train_set['hour_bef_pm2.5'])[0]
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
        for i in train_set.index:
            if i not in lead_outlier_index :
                lead_not_outlier_index.append(i)
        train_set_clean = train_set.loc[lead_not_outlier_index]      
        train_set_clean = train_set_clean.reset_index(drop=True)
        print(train_set_clean)

    def learning(self):
        train_set_clean = self.train_set_clean
        x = train_set_clean.drop(['count'],axis=1) #axis는 컬럼 
        print(x.columns)
        print(x.shape) #(1459, 9)

        y = train_set_clean['count']
        
        x = np.array(x)
        y = np.array(y)

        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, train_size=0.7, random_state=1234)

        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)

        #2. 모델
        
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

    def test(self):
        #4. 평가, 예측
        x_test = self.x_test
        y_test = self.y_test
        model = self.model
        print('model.score :',model.score(x_test,y_test))