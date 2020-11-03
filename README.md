# data_wrangling

**_dfg(dataframe, group_by, select)_ function takes as an input a datarame of the following format:**

|  Year  |  AIS  |  SJR  |   B   |  C  | 
|--------|-------|-------|-------|-----|
|  2012  | 11202 | 23005 | 909.8 | 400 |
|  2013  | 13400 | 25600 | 800   | 200 |
|  2014  | 13987 | 27000 | 2310  | 325 |
|  2015  | 15044 | 29876 | 1708  | 200 |
|  2016  | 16234 | 31051 | 1200  | 300 |
|  2017  | 18001 | 35015 | 998   | 777 |

**and based on specified parameters returns reorganized dataframe, e.g. _dfg(sample_data, "Year", ["B", "C"])**
