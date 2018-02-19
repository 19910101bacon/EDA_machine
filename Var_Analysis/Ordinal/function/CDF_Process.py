

def cdf_process(Data, Data_group, text):
    result = []

    values = Data_group[Data_group.cdf <= 0.25]['value'].tolist()
    Index = Data[Data.value.isin(values)]['index'].tolist()
    result.append({text + '~20%' : Index})

    values = Data_group[(Data_group.cdf > 0.25) & (Data_group.cdf <= 0.75)]['value'].tolist()
    Index = Data[Data.value.isin(values)]['index'].tolist()
    result.append({text + '25~75%' : Index})

    values = Data_group[(Data_group.cdf > 0.75) ]['value'].tolist()
    Index = Data[Data.value.isin(values)]['index'].tolist()
    result.append({text + '75~%' : Index})


    return(result)
