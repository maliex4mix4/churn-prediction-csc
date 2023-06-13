import pandas as pd
from ms import model


def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction


def get_model_response(json_data):

    standard_cols = [
        'Tenure',
        'WarehouseToHome',
        'HourSpendOnApp',
        'NumberOfDeviceRegistered',
        'SatisfactionScore',
        'NumberOfAddress',
        'Complain',
        'OrderAmountHikeFromlastYear',
        'CouponUsed',
        'OrderCount',
        'DaySinceLastOrder',
        'CashbackAmount',
        'PreferredLoginDevice_Computer',
        'PreferredLoginDevice_Phone',
        'CityTier_150k to 3 mln',
        'CityTier_3 to 15 mln',
        'CityTier_over 15 mln',
        'PreferredPaymentMode_Cash on Delivery',
        'PreferredPaymentMode_Credit Card',
        'PreferredPaymentMode_Debit Card',
        'PreferredPaymentMode_E wallet',
        'PreferredPaymentMode_UPI',
        'Gender_Female',
        'Gender_Male',
        'PreferedOrderCat_Fashion',
        'PreferedOrderCat_Grocery',
        'PreferedOrderCat_Laptop & Accessory',
        'PreferedOrderCat_Mobile',
        'PreferedOrderCat_Mobile Phone',
        'PreferedOrderCat_Others',
        'MaritalStatus_Divorced',
        'MaritalStatus_Married',
        'MaritalStatus_Single'
    ]
    
    X = pd.DataFrame.from_dict(json_data)
    
    new = pd.get_dummies(X)

    # print(new.head())

    remaining_cols = [x for x in standard_cols if x not in new]

    # print(remaining_cols)
    cols_df = pd.DataFrame(columns=remaining_cols)

    # cols_df.fillna(value=0, inplace=True)

    final_df = pd.concat([new, cols_df], axis=1)

    final_df.fillna(0, inplace=True)

    final_df.replace(True, 1, inplace=True)

    # print(final_df.head(5))

    
    prediction = predict(final_df, model)

    # print(prediction)
    
    if prediction == 1:
        label = "Churn"
    else:
        label = "No Churn"
    
    return {
        'status': 200,
        'label': label,
        'prediction': int(prediction)
    }