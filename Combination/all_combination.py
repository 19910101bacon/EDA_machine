import itertools

class Combination:
    def __init__(self, data):
        self.data = data

    def permutations(self, num):
        All_Combination = []
        for i in range(num):
            Var_Index = list(range(self.data.shape[1]))  # 取index
            Var_Name = self.data.iloc[0,:].tolist()  # 取欄位名稱
            Combination_Index = list(itertools.permutations(Var_Index ,i+1))
            Combination_Name = list(itertools.permutations(Var_Name ,i+1))
            All_Combination = All_Combination + [dict(zip(Combination_Index[j], Combination_Name[j])) for j in range(len(Combination_Index))]
        return(All_Combination)

if __name__ == '__main__':
    import pandas as pd
    Adjust_Var = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/Independent_Var.csv', encoding = 'big5', header = None)
    result = Combination(Adjust_Var)
    print(len(result.permutations(3)))
