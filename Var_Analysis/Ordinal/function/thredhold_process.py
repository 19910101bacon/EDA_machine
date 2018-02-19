

def ordinal_threshold(Data, Data_group, text) :
    check = Data_group['check'].tolist()
    value_combination = []
    tem_comb = []
    for i in range(len(check)) :
        if check[i] == 1:
            tem_comb.append(Data_group.iloc[i, 0])
        else :
            value_combination.append(tem_comb)
            tem_comb = []
    value_combination.append(tem_comb)
    value_combination = [x for x in value_combination if len(x) > 0]

    result = []
    for i in range(len(value_combination)):
        MAX = max(value_combination[i])
        MIN = min(value_combination[i])

        s_text = text + str(MIN) + ' ~ ' + str(MAX)
        s_data = Data[Data.value.isin(value_combination[i])]
        result.append({s_text : s_data['index'].tolist()})

    return(result)
