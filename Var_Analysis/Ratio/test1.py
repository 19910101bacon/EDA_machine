
import itertools

class Combination:
    def __init__(self, data):
        self.data = data

    def permutations(self, num):
        All_Combination = []
        for i in range(num):
            Var_Index = list(range(self.data.shape[1]))
            Var_Name = self.data.iloc[0,:].tolist()
            Combination_Index = list(itertools.permutations(Var_Index ,i+1))
            Combination_Name = list(itertools.permutations(Var_Name ,i+1))
            All_Combination = All_Combination + [dict(zip(Combination_Index[j], Combination_Name[j])) for j in range(len(Combination_Index))]
        return(All_Combination)
import pandas as pd

Adjust_Var = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/Independent_Var.csv', encoding = 'big5', header = None)

condition_num = 2
All_Combination = Combination(Adjust_Var).permutations(condition_num)

i = 45 ; j = 1
Data = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/United_Feature_article.csv', encoding = 'big5')
var = {list(All_Combination[i].keys())[j] : list(All_Combination[i].values())[j]}
Index = [{'' : list(range(len(Data)))}]
index = list(Index[0].values())[0]



import matplotlib.pyplot as plt
plt.hist(Data['麼'].tolist(), bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()

quit()
#class Ratio:
#x = Data_tem, group = i
def cdf_process(x, group, text):
    result = []
    data_group = x[x.group == i]
    Index = data_group[data_group.cdf <= 0.05]['index'].tolist()
    result.append({text + '~5%' : Index})

    Index = data_group[(data_group.cdf > 0.05) & (data_group.cdf < 0.25)]['index'].tolist()
    result.append({text + '5~25%' : Index})

    Index = data_group[(data_group.cdf > 0.25) & (data_group.cdf < 0.75)]['index'].tolist()
    result.append({text + '25~75%' : Index})

    Index = data_group[(data_group.cdf > 0.75) & (data_group.cdf < 0.95)]['index'].tolist()
    result.append({text + '75~95%' : Index})

    Index = data_group[data_group.cdf > 0.95]['index'].tolist()
    result.append({text + '95~%' : Index})

    Index = data_group[(data_group.cdf > 0.05) & (data_group.cdf < 0.95)]['index'].tolist()
    result.append({text + '5~95%' : Index})

    Index = data_group[(data_group.cdf >= 0) & (data_group.cdf <= 1)]['index'].tolist()
    result.append({text + '0~100%' : Index})
    return(result)

Data_var = Data[''.join(list(var.values()))].tolist()  # select series from data by variable
data = [Data_var[i] for i in index] # select element by index
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
data_arr = np.asarray(data)


if len(data)/len(Data_var) > 0.01 :

    result = pd.DataFrame(columns = ['tot_variance', 'rate_of_min_sample'])
    for i in range(5):
        try:
            kmeans = KMeans(n_clusters = i+1, random_state = 0).fit(data_arr.reshape(-1,1))
            total_var = kmeans.inertia_

            a = list(dict(Counter(kmeans.labels_)).values())
            sample_rate_min = min(a/np.sum(a))
            result.loc[i] = [total_var, sample_rate_min]
        except:
            result.loc[i] = [404, 404]
    num_check = (result['rate_of_min_sample'] > 0.15).tolist()
    variance_check = (result['tot_variance'][0]/result['tot_variance'].tolist() >= [1, 3, 10, 20, 30]).tolist()
    a = [num_check[i]*variance_check[i] for i in range(5)]
    b = [i for i,x in enumerate(a) if x == 1]

    group_num = max(b) + 1
    kmeans = KMeans(n_clusters = group_num, random_state = 0).fit(data_arr.reshape(-1,1))
    #print(list(kmeans.labels_))
    Data_tem = pd.DataFrame({'group' : list(kmeans.labels_), 'index' : index, 'value' : list(data_arr)}).sort_values(['group', 'value'])
    group_element = Data_tem.groupby('group').count().iloc[:,0].tolist()
    Data_tem['cdf'] = [(j+1)/i for i in group_element for j in range(i)]

    result = []
    for i in range(group_num):
        a = Data_tem[Data_tem['group'] == i]['index'].tolist()
        Max = max(Data_tem[Data_tem['group'] == i]['value'])
        Min = min(Data_tem[Data_tem['group'] == i]['value'])
        text = ''.join(list(var.values())) + ': 分' + str(group_num) + '群，'

        result = result + cdf_process(Data_tem, i, text)
        print(result)

quit()


## test
x1 = np.random.normal(0, 0.2, 500)
x2 = np.random.normal(0.4, 0.2, 500)
x3 = np.random.normal(0.9, 0.2, 100)

x4 = np.asarray(list(x1) + list(x2) + list(x3))



kmeans = KMeans(n_clusters = 1, random_state = 0).fit(x4.reshape(-1,1))
g1 = kmeans
kmeans = KMeans(n_clusters = 2, random_state = 0).fit(x4.reshape(-1,1))
g2 = kmeans
kmeans = KMeans(n_clusters = 3, random_state = 0).fit(x4.reshape(-1,1))
g3 = kmeans
kmeans = KMeans(n_clusters = 4, random_state = 0).fit(x4.reshape(-1,1))
g4 = kmeans

from collections import Counter
a = list(dict(Counter(g1.labels_)).values())
b = a/np.sum(a)
print(min(b)) ; print(g1.inertia_)

a = list(dict(Counter(g2.labels_)).values())
b = a/np.sum(a)
print(min(b)) ; print(g1.inertia_/g2.inertia_)

a = list(dict(Counter(g3.labels_)).values())
b = a/np.sum(a)
print(min(b)) ; print(g1.inertia_/g3.inertia_)

a = list(dict(Counter(g4.labels_)).values())
b = a/np.sum(a)
print(min(b)) ; print(g1.inertia_/g4.inertia_)




################

import matplotlib.pyplot as plt
plt.hist(list(x4), bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()
