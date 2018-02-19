

def cdf_process(x, group, text):
    result = []
    data_group = x[x.group == group]
    Index = data_group[data_group.value == 0]['index'].tolist()
    result.append({text + 'all 0' : Index})

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

    return(result)
