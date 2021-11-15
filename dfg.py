import pandas as pd

def dfg(dataframe, group_by, select):
    """Transforms dataset input based
    on parameters - group_by, select.
    Duplicates rows based on group_by
    while transforming only selected
    variables, e.g.:
    
    | Year | AIS | SJR | B | C |
    ----------------------------
    | 2012 | 112 | 300 | 8 | 4 |
    
    dfg(dataframe, "Year", ["B", "C"])
    
    | Year | Values | Type |
    ------------------------
    | 2012 |	 B    |  8 |
    | 2012 |	 C    |  4 |
    
    """
    output=pd.DataFrame()
    group_by_=[[_]*len(select) for _ in dataframe[group_by]]
    output[group_by]=[_ for l in group_by_ for _ in l]
    rows=[_ for _ in range(len(dataframe))]
    values=[dataframe[select].loc[_] for _ in rows]
    output["values"]=[_ for l in values for _ in l]
    output["type"]=select*len(dataframe)
    return output
