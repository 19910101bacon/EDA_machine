# input : Data, current_var, Index
try :
    from Var_Analysis.Ratio.function.Kmeans_Selection import group_num
    from Var_Analysis.Ratio.function.CDF_Process import cdf_process
except :
    from function.Kmeans_Selection import group_num
    from function.CDF_Process import cdf_process

import pandas as pd

import numpy as np
from sklearn.cluster import KMeans

def Ratio(Data, current_var, Index):
    # current_var : dict with one key
    # Index : list of dicts, which having text and index
    result = []

    for cur_condition in Index :
        #print(cur_condition)
        index = list(cur_condition.values())[0]

        if len(index) < 50 or (len(index)/Data.shape[0]) < 0.01:
            result = result + [cur_condition]
        else :
            Data_var = Data[''.join(list(current_var.values()))].tolist()  # select series from data by variable
            data = [Data_var[i] for i in index] # select element by index
            data_arr = np.asarray(data)

            group_number = group_num(data_arr) # decide clustering number
            kmeans = KMeans(n_clusters = group_number, random_state = 0).fit(data_arr.reshape(-1,1))

            Data_tem = pd.DataFrame({'group' : list(kmeans.labels_), 'index' : index, 'value' : list(data_arr)}).sort_values(['group', 'value'])
            group_element = Data_tem.groupby('group').count().iloc[:,0].tolist()
            Data_tem['cdf'] = [(j+1)/i for i in group_element for j in range(i)]

            original_text = list(cur_condition.keys())[0]

            for i in range(group_number):
                a = Data_tem[Data_tem['group'] == i]['index'].tolist()
                Max = max(Data_tem[Data_tem['group'] == i]['value'])
                Min = min(Data_tem[Data_tem['group'] == i]['value'])
                text = original_text + ' & ' + ''.join(list(current_var.values())) + '- 分' + str(group_number) + '群 : '

                result = result + cdf_process(Data_tem, i, text)
    return(result)

if __name__ == '__main__':
    Data = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/United_Feature_article.csv', encoding = 'big5')
    #current_var = {1: '們'}
    #current_var = {1: '們'}
    current_var = {2: '個'}
    #current_var = {4: '和'}
    #current_var = {3: '了'}
    #current_var = {5: '麼'}
    #current_var = {7: '嗎'}

    #Index = [{' & 們: 分1群，~5%': [28, 71, 135, 190, 201, 257, 357, 523, 661, 787, 799, 846, 847, 874, 880, 888, 925, 938, 943, 976, 1005, \
    #1016,1034, 1035, 1042, 1057, 1064, 1069, 1076, 1079, 1093, 1095, 1096, 1103, 1108, 1110, 1113, 1131, 1234, 1249, 1252, 1255, 1260, 1270,\
    # 1278, 1293, 1299, 1311, 1315, 1319, 1326, 1364, 1374, 1482, 1483, 1582, 1648, 906, 1604, 896, 978, 732, 1500, 1012, 316, 837, 859, 963 \
    # , 853, 653, 385, 1043, 1275, 902, 981, 749, 1060, 111, 898, 816, 379, 894]}]
    Index = [{'': list(range(Data.shape[0]))}]
    a = Ratio(Data, current_var, Index)
    current_var = {8: '吧'}
    b = Ratio(Data, current_var, a)
    print(a)
