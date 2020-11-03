import pandas as pd

def dfg(dataframe, group_by, select):
    output=pd.DataFrame()
    group_by_=[[_]*len(select) for _ in dataframe[group_by]]
    output[group_by]=[_ for l in group_by_ for _ in l]
    rows=[_ for _ in range(len(dataframe))]
    values=[dataframe[select].loc[_] for _ in rows]
    output["values"]=[_ for l in values for _ in l]
    output["type"]=select*len(dataframe)
    return output
