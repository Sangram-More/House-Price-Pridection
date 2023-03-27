def ChooseModel(model_name, area, no_of_bedrooms, city, location, resale):
    
    if model_name == 'Linear Regression':
        LinearRegressionPrediction(area, no_of_bedrooms, city, location, resale)
    
    if model_name == 'Ridge Regression':
        RidgeRegressionPrediction(area, no_of_bedrooms, city, location, resale)

    if model_name == 'Decision Tree':
        DecisionTreePrediction(area, no_of_bedrooms, city, location, resale)
    
    if model_name == 'Random Forest':
        RandomForestPrediction(area, no_of_bedrooms, city, location, resale)
    
    if model_name == 'XGBoost':
        XGBoostPrediction(area, no_of_bedrooms, city, location, resale)

#-------------------------------------------------------------------------------------------------

def LinearRegressionPrediction(area, no_of_bedrooms, city, location, resale):
    from sklearn import linear_model
    from sklearn.linear_model import LinearRegression
    LR = LinearRegression()
    LR.fit(X_train, y_train)
    y_predict_LR = LR.predict(X_test)

    input = [[area, no_of_bedrooms, city, location, resale]]
    y_predict_LR_Single = LR.predict(input)
    print(y_predict_LR_Single)
    # print(y_predict_LR)
    # LR_score = LR.score(X_test, y_test)
    # print(LR_score*100)
    # Cross Validation
    # CVS_LR = cross_val_score(LR, data, price, cv=10).mean()
    # CVP_LR= cross_val_predict(LR, X_test, y_test,  cv=10)

#------------------------------------------------------------------------------------------------- 

def RidgeRegressionPrediction(area, no_of_bedrooms, city, location, resale):
    from sklearn.linear_model import Ridge
    from sklearn.model_selection import GridSearchCV
    RR = Ridge()
    RR.fit(X_train,y_train)
    y_predict_RR = RR.predict(X_test)
    
    input = [[area, no_of_bedrooms, city, location, resale]]
    y_predict_RR_Single = RR.predict(input)
    print(y_predict_RR_Single)
    # print(y_predict_RR)
    # RR_score = RR.score(X_test, y_test)
    # print(RR_score*100)
    # CVS_RR = cross_val_score(RR, data, price, cv=10).mean()
    # CVP_RR = cross_val_predict(RR, X_test, y_test,  cv=10)

#-------------------------------------------------------------------------------------------------

def DecisionTreePrediction(area, no_of_bedrooms, city, location, resale):
    from sklearn.tree import DecisionTreeRegressor
    DT = DecisionTreeRegressor(max_depth=5)
    DT.fit(X_train,y_train)
    y_predict_DT = DT.predict(X_test)

    input = [[area, no_of_bedrooms, city, location, resale]]
    y_predict_DT_Single = DT.predict(input)
    print(y_predict_DT_Single)
    # DT_score = DT.score(X_test, y_test)
    # Cross Validation
    # CVS_DT = cross_val_score(DT, data, price, cv=10).mean()
    # CVP_DT= cross_val_predict(DT, X_test, y_test,  cv=10)

#-------------------------------------------------------------------------------------------------

def RandomForestPrediction(area, no_of_bedrooms, city, location, resale):
    from sklearn.ensemble import RandomForestRegressor
    RF = RandomForestRegressor(n_estimators=280, random_state=0)
    RF.fit(X_train, y_train)
    y_predict_RF = RF.predict(X_test)
    RF_score = RF.score(X_test, y_test)

    input = [[area, no_of_bedrooms, city, location, resale]]
    y_predict_RF_Single = RF.predict(input)
    print(y_predict_RF_Single)
    # Cross Validation
    # CVS_RF = cross_val_score(RF, data, price, cv=10).mean()
    # CVP_RF = cross_val_predict(RF, X_test, y_test,  cv=10)
#-------------------------------------------------------------------------------------------------

def XGBoostPrediction(area, no_of_bedrooms, city, location, resale):
    from xgboost import XGBRegressor
    XGB = XGBRegressor()
    XGB.fit(X_train, y_train)
    y_predict_XGB = XGB.predict(X_test)
    
    input = {
    'Area' : [area],
    'No. of Bedrooms' : [no_of_bedrooms], 
    'City' : [city], 
    'Location' : [location], 
    'Resale' : [resale]
    }

    frame = df = pd.DataFrame(input)
    y_predict_XGB_single = XGB.predict(frame)
    print(y_predict_XGB_single)
    # XGB_score = XGB.score(X_test, y_test)
    # Cross Validation
    # CVS_XGB = cross_val_score(XGB, data, price, cv=10).mean()
    # CVP_XGB = cross_val_predict(XGB, X_test, y_test,  cv=10)

# -----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import MinMaxScaler, LabelEncoder, OneHotEncoder
    from sklearn.model_selection import train_test_split,  cross_val_score, cross_val_predict
    from sklearn.metrics import r2_score, confusion_matrix
    from sklearn import metrics

    import sys
    area = int(sys.argv[1])
    no_of_bedrooms = int(sys.argv[2])
    city = str(sys.argv[3])
    location = str(sys.argv[4])
    resale = int(sys.argv[5])
    model_name = str(sys.argv[6])

    df = pd.read_csv('../CSV/India.csv', index_col=False)

    # Label Encoding
    label_encoder = LabelEncoder()
    # print(label_encoder)
    df_encoded = df.copy()
    df_encoded['Location'] = label_encoder.fit_transform(df['Location'])
    Location_name_mapping = dict(zip(label_encoder.classes_,    label_encoder.transform(label_encoder.classes_)))
    # print(Location_name_mapping)
    df_encoded['City'] = label_encoder.fit_transform(df['City'])
    city_name_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
    # print(city_name_mapping)

    df1 = df_encoded[['Price','Area', 'No. of Bedrooms', 'City', 'Location', 'Resale']]
    df1.head()

    # Dependent - Independent Variables
    df_temp = df1.copy()
    data = df_temp.drop('Price', axis=1)
    price = df_temp['Price']

    # Train Test split
    X_train, X_test, y_train, y_test = train_test_split(data, price, test_size=0.2)
    # print(len(X_train), len(X_test), len(y_train), len(y_test))

    #Parameters
    # area = 3340
    # no_of_bedrooms = 4
    city = int(city_name_mapping.get(city))
    location = int(Location_name_mapping.get(location))
    # resale = 0
    # model_name = 'XGBoost'


    ChooseModel(model_name, area, no_of_bedrooms, city, location, resale)

# ---------------------------------------------------------------------------------------------------------------

