import requests
import json
import pandas as pd
import numpy as np

def plot_data(date1,date2,id):

    df_real_assets = pd.read_csv("data/df_real_assets.csv")
    headers = {
        'accept': 'application/json',
    }

    params = (
        ('from_date', date1),
        ('to_date', date2),
    )

    real_asset =df_real_assets[df_real_assets.id==id]
    real_assets_id = int(real_asset.id)

    response = requests.get('https://fintual.cl/api/real_assets/'+str(real_assets_id)+'/days', headers=headers, params=params)

    rt = response.text
    data = json.loads(rt)

    df_real_assets_days = pd.DataFrame()

    for i in range(np.shape(data['data'])[0]):
        uno = pd.DataFrame([data['data'][i]['attributes']])
        dos = pd.DataFrame([data['data'][i]['id'],data['data'][1]['type']], index = ['id','type']).T

        day = pd.concat([dos,uno], axis=1)
        
        df_real_assets_days = pd.concat([df_real_assets_days,day], ignore_index=True)

    return df_real_assets_days