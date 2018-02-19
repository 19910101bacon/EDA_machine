import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
import pandas as pd

def group_num(x):
    result = pd.DataFrame(columns = ['tot_variance', 'rate_of_min_sample'])
    for i in range(5):
        try:
            kmeans = KMeans(n_clusters = i+1, random_state = 0).fit(x.reshape(-1,1))
            total_var = kmeans.inertia_
            if total_var == 0:
                total_var = 0.00000000001

            a = list(dict(Counter(kmeans.labels_)).values())
            sample_rate_min = min(a/np.sum(a))
            result.loc[i] = [total_var, sample_rate_min]
        except:
            result.loc[i] = [404, 404]

    num_check = (result['rate_of_min_sample'] > 0.2).tolist()
    #print(result['rate_of_min_sample'])

    variance_check = (result['tot_variance'][0]/result['tot_variance'].tolist() >= [1, 3.2, 10, 20, 30]).tolist()
    #print(result['tot_variance'][0]/result['tot_variance'].tolist())
    a = [num_check[i]*variance_check[i] for i in range(5)]
    b = [i for i,x in enumerate(a) if x == 1]
    group_num = max(b) + 1

    return(group_num)
