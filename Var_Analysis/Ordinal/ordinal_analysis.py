# input : Data, current_var, Index
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from Var_Analysis.Ordinal.function.thredhold_process import ordinal_threshold
from Var_Analysis.Ordinal.function.CDF_Process import cdf_process

def Ordinal(Data, current_var, Index):
    # current_var : dict with one key
    # Index : list of dicts, which having text and index
    result = []

    for cur_condition in Index :
        index = list(cur_condition.values())[0]

        if len(index) < 50 or (len(index)/Data.shape[0]) < 0.01:
            result = result + [cur_condition]
        else :
            Data_var = Data[''.join(list(current_var.values()))].tolist()  # select series from data by variable
            data = [Data_var[i] for i in index]

            Data_tem = pd.DataFrame({'index' : index, 'value' : data})
            Data_tem1 = Data_tem.groupby('value').size().reset_index(name='counts').sort_values('value')
            Data_tem1['counts'] = Data_tem1['counts']/np.sum(Data_tem1['counts'])


            Data_tem1['check'] = (1*(Data_tem1['counts'] >= 1/(3*Data_tem1.shape[0]))).tolist()
            original_text = list(cur_condition.keys())[0]
            s_text = original_text + ' & ' + list(current_var.values())[0] + '(常用) : '

            result = result + ordinal_threshold(Data_tem, Data_tem1, s_text)

            Data_tem1['cdf'] = [(i+1)/Data_tem1.shape[0] for i in list(range(Data_tem1.shape[0]))]
            s_text = original_text + ' & ' + list(current_var.values())[0] + '(分位) : '
            result = result + cdf_process(Data_tem, Data_tem1, s_text)
    return(result)


if __name__ == '__main__':
    Data = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/United_Feature_article.csv', encoding = 'big5')
    current_var = {0: 'Year'}

    Index = [{'': list(range(Data.shape[0]))}]
    a = Ordinal(Data, current_var, Index)
    #current_var = {7: '嗎'}
    #b = Ratio(Data, current_var, a)
    print(a)
