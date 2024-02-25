import pandas as pd
import numpy as np
import math
import json
def clean_file(filename):
    df = pd.read_csv(filename, encoding="unicode_escape")

    feature_columns = ["Size_Class","Curb_Wgt","ABS","Airbag_D","SSF","Drive","Drive4","TireSize",
                    "StabilityControl","BrakeAssist","TractionControl","AdjUpperBeltFront","AdjUpperBeltRear",
                    "Pretensioner","IntegratedSeat","RearCtrLapShldrBelt","AdvanceAirbagFeature","SideAirbag",
                    "HeadAirbag","HeadAirbagRollover","RearSeatHeadRestraint","DynamicHeadRestraint",
                    "Roll_Stability","SafetyPowerWindows","WheelsDriven", "DrStar_Num", "PaStar_Num", "DrSSTar_Num", "PaSStar_Num"]

    df_features = df[feature_columns]

    y_features = ["DrStar_Num", "PaStar_Num", "DrSSTar_Num", "PaSStar_Num"]
    true_false_features = ["ABS","Airbag_D","StabilityControl","BrakeAssist","TractionControl","AdjUpperBeltFront","AdjUpperBeltRear","Pretensioner","IntegratedSeat",
    "RearCtrLapShldrBelt","AdvanceAirbagFeature","HeadAirbagRollover",
    "RearSeatHeadRestraint","DynamicHeadRestraint","Roll_Stability","SafetyPowerWindows"]
    used_indicators = ["Y", "S", "Std", "Yes"]
    for feature in true_false_features:
        df_features[feature] = df_features[feature].fillna(False)
        df_features[feature] = df_features[feature].isin(used_indicators)
    for feature in y_features:
        df_features[feature] = df_features[feature].fillna(-1)
        df_features[feature] = np.floor(df_features[feature]).astype(int)
        df_features[feature] = df_features[feature].apply(lambda x: x-10 if 11 <= x <= 15 else x)
        df_features[feature] = df_features[feature] - 1
        df_features.loc[df_features[feature].between(5, 40), feature] = pd.NA

        # Convert the column to a nullable integer type
        df_features[feature] = df_features[feature].astype('Int64')
        df_features[feature] = df_features[feature].replace(-1, pd.NA).astype('Int64')
    
    df_features['Drive'] = df_features['Drive'].combine_first(df_features['Drive4'])
    df_features.drop('Drive4', axis=1, inplace=True)
    df['WheelsDriven'] = df['WheelsDriven'].fillna(df['Drive'])

    df['Drive'] = df['Drive'].fillna(df['WheelsDriven'])
    df_features['Curb_Wgt'] = df_features['Curb_Wgt'].apply(pd.to_numeric, errors='coerce')
    df_features['SSF'] = df_features['SSF'].apply(pd.to_numeric, errors='coerce')

    df_features[['Width', 'AspectRatio', 'WheelDiameter']] = df_features['TireSize'].str.extract(r'P(\d+)/(\d+)R(\d+)').astype(float)
    df_features['Width'] = df_features['Width'] / 25.4

    df_features['HeadAirbag'] = df_features['HeadAirbag'].notnull()
    df_features['SideAirbag'] = df_features['HeadAirbag'].notnull()

    # Calculate sidewall height in inches
    df_features['SidewallHeight'] = (df_features['AspectRatio'] / 100) * df_features['Width']
    df_features["TireSize"] = (2 * df_features['SidewallHeight']) + df_features['WheelDiameter']
    df_features = df_features.drop(["Width","AspectRatio","WheelDiameter","SidewallHeight"], axis = 1)
    df_features.dropna().reset_index().to_csv(f'cleaned_features_{filename}')

clean_file("NHTSACar.csv")