import pandas as pd
import xgboost as xgb
import numpy as np
from xgboost import XGBRegressor, XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import RandomizedSearchCV
# Assuming `df` is your DataFrame
filename = "../cleaned_features_NHTSACar.csv"
df = pd.read_csv(filename, encoding="unicode_escape")
categorical_columns = ['Size_Class', 'Drive', 'WheelsDriven', "ABS","Airbag_D","StabilityControl","BrakeAssist","TractionControl","AdjUpperBeltFront","AdjUpperBeltRear","Pretensioner","IntegratedSeat",
    "RearCtrLapShldrBelt","AdvanceAirbagFeature","SideAirbag","HeadAirbag","HeadAirbagRollover",
    "RearSeatHeadRestraint","DynamicHeadRestraint","Roll_Stability","SafetyPowerWindows"]  
numerical_columns = ['Curb_Wgt', 'SSF', 'TireSize']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numerical_columns),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
    ])

def get_model(judge):

    X = df.drop(['DrStar_Num', 'PaStar_Num', 'DrSSTar_Num', 'PaSStar_Num'], axis=1) 
    y = df[judge]
    X_processed = preprocessor.fit_transform(X)
    y = LabelEncoder().fit_transform(y)
    y[0] = 0
    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
    xgb_model = XGBClassifier(objective='multi:softmax')  # Set num_class to the number of classes

    parameters = {
        'n_estimators': [100, 500, 1000],
        'max_depth': [3, 5, 7, 10],
        'learning_rate': [0.01, 0.05, 0.1],
        'colsample_bytree': [0.3, 0.5, 0.7],
        'subsample': [0.5, 0.7, 1],
        'min_child_weight': [1, 3, 5],
        'alpha': [0, 0.5, 1],
        'lambda': [1, 1.5, 2]
        # You might want to adjust these parameters or add more based on your specific needs
    }

    random_search = RandomizedSearchCV(xgb_model, parameters, n_iter=25, scoring='accuracy', cv=5, verbose=1)  # Note the scoring metric change to 'accuracy'
    random_search.fit(X_train, y_train)

    print(random_search.best_params_)
    model = random_search.best_estimator_

    model.fit(X_train, y_train)

    print(model.score(X_test, y_test))
    return model

models = {}
for judge in ['DrStar_Num', 'PaStar_Num', 'DrSSTar_Num', 'PaSStar_Num']:
    models[judge] = get_model(judge)