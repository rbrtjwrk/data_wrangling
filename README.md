# data_wrangling

**dfg**

_dfg(dataframe, group_by, select)_ function takes as an input a datarame of the following format:

|  Year  |  AIS  |  SJR  |   B   |  C  | 
|--------|-------|-------|-------|-----|
|  2012  | 11202 | 23005 | 909.8 | 400 |
|  2013  | 13400 | 25600 | 800   | 200 |
|  2014  | 13987 | 27000 | 2310  | 325 |
|  2015  | 15044 | 29876 | 1708  | 200 |
|  2016  | 16234 | 31051 | 1200  | 300 |
|  2017  | 18001 | 35015 | 998   | 777 |

And based on specified parameters returns reorganized dataframe, e.g. for _dfg(dataframe, "Year", ["B", "C"])_ we get:

|  Year  | Values |  Type |
|--------|--------|-------|
|  2012  | 909.8  | B     |
|  2012  | 400    | C     |
|  2013  | 800    | B     |
|  2013  | 200    | C     |
|  2014  | 2310   | B     |
|  2014  | 325    | C     |
|  2015  | 1708   | B     |
|  2015  | 200    | C     |
|  2016  | 1200   | B     |
|  2016  | 300    | C     |
|  2017  | 998    | B     |
|  2017  | 777    | C     |

Which is quite useful if we want to further visualize the data using ggplot2.


**docx_to_txt**

_process_docx_to_txt(directory)_ function processes all .docx files in given directory into .txt files.
