import pandas as pd
import itertools

from Combination.all_combination import Combination
from Var_Analysis.Ratio.ratio_analysis import Ratio
from Var_Analysis.Ordinal.ordinal_analysis import Ordinal
from Correlation.All_type_pair_analysis import Pair_Var_Analysis
## input :
Data = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/United_Feature_article.csv', encoding = 'big5')
Adjust_Var = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/Independent_Var.csv', encoding = 'big5', header = None)
Target_Var = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/Dependent_Var.csv', encoding = 'big5', header = None)


#a = [zip(x,target_var) for x in itertools.permutations(adjust_var,len(target_var))]
#print(adjust_var)
#print(target_var)
#print(Var_pair)
## control
condition_num = 3

All_Combination = Combination(Adjust_Var).permutations(condition_num)  ## class class 'Combination'

k = 0
result = pd.DataFrame(columns = ['cond_1', 'range_1', 'cond_2', 'range_2', 'cond_3', 'range_3', 'x_var', 'y_var', 'corr', 'num', 'num_rate'])
result = result.append(Pair_Var_Analysis(Data, [{'' : list(range(Data.shape[0]))}], Adjust_Var, Target_Var, condition_num, 0.7))

for i in range(len(All_Combination)):
    Index = [{'': list(range(Data.shape[0]))}]


    num = len(list(All_Combination[i].keys()))

    for j in range(num):
        var = {list(All_Combination[i].keys())[j] : list(All_Combination[i].values())[j]}
        if Adjust_Var.iloc[1,list(All_Combination[i].keys())[j]] == 'Ratio':
            Index = Ratio(Data, var, Index)
        elif Adjust_Var.iloc[1,list(All_Combination[i].keys())[j]] == 'Ordinal':
            Index = Ordinal(Data, var, Index)
        result = result.append(Pair_Var_Analysis(Data, Index, Adjust_Var, Target_Var, condition_num, 0.7))

    if i > 100:
        print(result)
        quit()
