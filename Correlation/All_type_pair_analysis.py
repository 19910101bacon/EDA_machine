import itertools
from scipy.stats.stats import pearsonr
from sklearn import tree
from sklearn.metrics import accuracy_score
import re
import pandas as pd

def Pair_Var_Analysis(Data, Index, Adjust_Var, Target_Var, condition_num, threshold) :
    adjust_var_name = Adjust_Var.iloc[0,:].tolist()
    adjust_var_type = Adjust_Var.iloc[1,:].tolist()
    target_var_name = Target_Var.iloc[0,:].tolist()
    target_var_type = Target_Var.iloc[1,:].tolist()
    Var_pair = list(itertools.product(adjust_var_name, target_var_name))

    result = pd.DataFrame(columns = ['cond_1', 'range_1', 'cond_2', 'range_2', 'cond_3', 'range_3', 'x_var', 'y_var', 'corr', 'num', 'num_rate'])
    k = 0

    for i in range(len(Index)): ## all possible condition. in each condition ...


        text = list(Index[i].keys())[0]
        index = list(Index[i].values())[0]
        if len(index) <= 30:
            pass
        else :
            Data_f = Data.iloc[index,:]
            for m in range(len(Var_pair)): # every possible var_pair under each one condition
                Data_ff = Data_f[list(Var_pair[m])]
                x_var = Data_ff.iloc[:,0].tolist()
                y_var = Data_ff.iloc[:,1].tolist()

                Adjust_Var.columns = Adjust_Var.iloc[0,:].tolist()
                Target_Var.columns = Target_Var.iloc[0,:].tolist()

                x_var_name = Adjust_Var[Var_pair[m][0]].tolist()[0]
                y_var_name = Target_Var[Var_pair[m][1]].tolist()[0]

                x_var_type = Adjust_Var[Var_pair[m][0]].tolist()[1]
                y_var_type = Target_Var[Var_pair[m][1]].tolist()[1]

                if (x_var_type == 'Ordinal') & (y_var_type == 'Ratio'):
                    try:
                        Data_fff = Data_ff.groupby(x_var_name)[y_var_name].median().reset_index(name=y_var_name)
                        x = Data_fff[x_var_name].tolist()
                        y = Data_fff[y_var_name].tolist()

                        cor = pearsonr(x,y)[0]
                        num = len(x)
                        num_rate = num/Data.shape[0]
                    except:
                        cor = 0
                        num = 0
                        num_rate = 0


                elif (x_var_type == 'Ratio') & (y_var_type == 'Ratio'):
                    try:
                        cor = pearsonr(x_var, y_var)[0]
                        num = len(x_var)
                        num_rate = num/Data.shape[0]
                    except:
                        cor = 0
                        num = 0
                        num_rate = 0
                elif (x_var_type == 'Ratio') & (y_var_type == 'Nominal'):
                    try:
                        X = [[x] for x in x_var]
                        Y = y_var
                        clf = tree.DecisionTreeClassifier(max_depth=1)
                        clf = clf.fit(X, Y)
                        Y_pred = clf.predict(X)
                        cor = accuracy_score(Y, Y_pred)
                        num = len(x_var)
                        num_rate = num/Data.shape[0]
                    except:
                        cor = 0
                        num = 0
                        num_rate = 0
                else :
                    cor = 0
                    num = 0
                    num_rate = 0
                    pass
                text_p = re.split('&|:', text) ; text_p.pop(0)
                while len(text_p) != 2*condition_num:
                    text_p.append('nan')
                text_p = text_p + [x_var_name, y_var_name, cor, num, num_rate]
                if abs(cor) > threshold :
                    result.loc[k] = text_p
                    k += 1
    return(result)




if __name__ == '__main__':
    import pandas as pd
    Data = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/United_Feature_article.csv', encoding = 'big5')
    Adjust_Var = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/Independent_Var.csv', encoding = 'big5', header = None)
    Target_Var = pd.read_csv('/Users/xiaopingguo/Desktop/114通道/Dependent_Var.csv', encoding = 'big5', header = None)

    Index = [{' & 一|二|三|四|五|六|七|八|九|十|零- 分1群 : 5~95% & 不- 分1群 : 75~95%': [713, 735, 525, 842, 949, 1210, 924, 530, 446, 1388,\
     790, 1516, 1137, 5, 447, 584, 69, 494, 310, 304, 318, 247, 1150, 221, 182, 1196, 1533, 500, 1540, 741, 1040, 109, 1038, 1021, 58,\
     935, 582, 753, 716, 1022, 1242, 8, 1230, 995, 1307, 1327, 1348, 453,148, 1608, 1433, 565, 1221, 328, 663, 1337, 698, 960, 130, 825,\
     359, 877, 482, 1207, 1424, 1505, 1649, 1534, 891, 1622, 403, 808, 1288, 1213, 286, 215, 537, 514, 308, 1650, 947, 18, 230, 1444, 1265,\
     191, 13, 1655, 1352, 1519, 105, 682, 521, 1491, 1041, 1628, 806, 1219, 1450, 1209, 39, 133, 30, 907, 186, 1285, 171, 921, 295, 110, 564,\
     1602, 524, 617, 1561, 771, 1611, 1190, 962, 1576, 1382, 285, 1000, 1151, 1526, 21, 1490, 179, 165, 455, 1538, 1652, 1475, 1369, 555, 163,\
     220, 1470, 1277, 1532, 1542, 365, 1392, 260, 219, 198, 377, 761, 150, 416, 742, 834, 279, 625, 637, 336, 66, 1562, 65, 593, 589, 270, 1051,\
     736, 4, 594, 1453, 193, 1520, 1554, 367, 176, 152,1456, 1324, 1052, 1564, 691, 1197, 287, 61, 1452, 1068, 307, 957, 1546, 952, 1126, 1654,\
     121, 887, 421, 1120, 1497, 419, 466, 430, 1449, 371, 678, 82, 117, 1627, 161, 146, 292, 974, 57, 441, 1467, 648, 11, 1204, 208, 248, 794, 980,\
     93, 28, 477, 95, 964, 1244, 493, 56, 580, 1499, 642, 1233, 223, 1326, 440, 1560, 1639, 15, 1416, 1488, 313, 1398, 1239, 91, 1140, 1298, 546, 108,\
     1566, 709, 1371, 498, 973, 1496, 1577, 155, 1115, 1117, 288, 618, 205, 1427, 41, 1226, 951, 259, 1403, 1269, 602, 1549, 70, 62, 102, 1136, 1281,\
     1436, 115, 0, 412, 692, 207, 331, 305, 1138, 17, 1049, 520, 22, 203, 1359, 284, 1033, 754, 1656, 1347, 43, 351, 1522, 910, 703, 1304, 941]}, \
     {' & 一|二|三|四|五|六|七|八|九|十|零- 分1群 : 5~95% & 不- 分1群 : 95~%': [327, 340, 903, 1174, 946, 1315, 959, 303, 1289, 517, 1582, 1295, 373, 939,\
     1361, 1010, 1555, 1156, 1227, 1492, 132, 366, 1610, 1557, 60, 849, 27, 664, 1430, 965, 1335, 693, 407, 1313, 581, 1440, 1483, 981, 142, 1296,\
     1044, 1339, 167, 1390, 515, 629, 1485, 240, 68, 1415, 1575, 2, 845, 283, 1262, 1612, 51, 1511, 414, 1185, 273, 250, 10, 1116, 1291, 1525, 348,\
     34, 151, 523, 267, 636, 1482, 656, 1260]}]
    threshold = 0.5

    a = Pair_Var_Analysis(Data, Index, Adjust_Var, Target_Var,3, threshold)
    print(a)
