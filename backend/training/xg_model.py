import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

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
        ('cat', OneHotEncoder(), categorical_columns)
    ])
def get_model(judge):

    X = df.drop(['DrStar_Num', 'PaStar_Num', 'DrSSTar_Num', 'PaSStar_Num'], axis=1) 
    y = df[judge]
    X_processed = preprocessor.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
    model = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                    max_depth = 5, alpha = 10, n_estimators = 10)

    model.fit(X_train, y_train)

    print(model.score(X_test, y_test))
    return model

models = {}
for judge in ['DrStar_Num', 'PaStar_Num', 'DrSSTar_Num', 'PaSStar_Num']:
    models[judge] = get_model(judge)