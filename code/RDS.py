import pickle
import pandas as pd
import ransom_preprocessing as rp

def list_to_df(ll, columns):
    return pd.DataFrame(ll, columns=columns)

def is_ransom_by_api(api_model_path, data_path):
    with open(api_model_path, 'rb') as f:
        api_saved_dict = pickle.load(f)
    api_model = api_saved_dict['model']

    # data 전처리
    pre_data_by_api = [rp.pre_api(data_path)]

    api_df = list_to_df(pre_data_by_api, rp.api_columns)
    return api_model.predict(api_df)

def is_ransom_by_sectionname(sn_model_path, data_path):
    with open(sn_model_path, 'rb') as f:
        sn_saved_dict = pickle.load(f)
    sn_model = sn_saved_dict['model']

    # data 전처리
    pre_data_by_sn = [rp.pre_sectionname(data_path)]

    sn_df = list_to_df(pre_data_by_sn, rp.sn_columns)
    return sn_model.predict(sn_df)
