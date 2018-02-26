# input : Data, current_var, Index
import pandas as pd
import numpy as np


def Nominal(Data, current_var, Index):
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
            original_text = list(cur_condition.keys())[0]
            var_name = list(set(Data_var))

            for i in range(len(var_name)) :
                Data_tem1 = Data_tem[Data_tem.value == var_name[i]]
                s_text = original_text + ' & ' + list(current_var.values())[0] + ' : ' + var_name[i]
                result = result + [{s_text : Data_tem1['index'].tolist()}]

    return(result)


if __name__ == '__main__':
    Data = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/United_Feature_article.csv', encoding = 'big5')
    current_var = {32: '分類'}

    Index = [{'': list(range(Data.shape[0]))}]
    a = Nominal(Data, current_var, Index)
    #current_var = {7: '嗎'}
    #b = Ratio(Data, current_var, a)
    print(a)
