import pickle
import pandas as pd
import binary_preprocessing as bp

def list_to_df(ll, columns):
    return pd.DataFrame(ll, columns=columns)

def is_malware_by_api(api_model_path, data_path):
    with open(api_model_path, 'rb') as f:
        api_saved_dict = pickle.load(f)
    api_model = api_saved_dict['model']

    # data 전처리
    pre_data_by_api = [bp.pre_api(data_path)]

    api_df = list_to_df(pre_data_by_api, bp.api_columns)
    return api_model.predict(api_df)

def is_malware_by_entropy(etrp_model_path, data_path):
    with open(etrp_model_path, 'rb') as f:
        etrp_saved_dict = pickle.load(f)
    etrp_model = etrp_saved_dict['model']

    # data 전처리
    pre_data_by_etrp = [bp.pre_entropy(data_path)]

    etrp_df = list_to_df(pre_data_by_etrp, bp.entropy_columns)
    return etrp_model.predict(etrp_df)

def is_malware_by_entrypoint(ep_model_path, data_path):
    with open(ep_model_path, 'rb') as f:
        ep_saved_dict = pickle.load(f)
    ep_model = ep_saved_dict['model']

    # data 전처리
    pre_data_by_ep = [bp.pre_entrypoint(data_path)]

    ep_df = list_to_df(pre_data_by_ep, bp.ep_columns)
    return ep_model.predict(ep_df)