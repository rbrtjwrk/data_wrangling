# data_wrangling

## data_for_plot

_data_for_plot(dataframe, group_by, select)_ function takes as an input a datarame of the following format:

|  Year  |  AIS  |  SJR  |   B   |  C  | 
|--------|-------|-------|-------|-----|
|  2015  | 15044 | 29876 | 1708  | 200 |
|  2016  | 16234 | 31051 | 1200  | 300 |
|  2017  | 18001 | 35015 | 998   | 777 |

And based on specified parameters returns reorganized dataframe, e.g. for _data_for_plot(dataframe, "Year", ["B", "C"])_ we get:

|  Year  | Values |  Type |
|--------|--------|-------|
|  2015  | 1708   | B     |
|  2015  | 200    | C     |
|  2016  | 1200   | B     |
|  2016  | 300    | C     |
|  2017  | 998    | B     |
|  2017  | 777    | C     |

Which is quite useful if we want to further visualize the data using ggplot2.  

## docx_to_txt

_process_docx_to_txt(directory)_ function processes all .docx files in given directory to .txt files.  


## onehot

_onehot(dataframe, labels_colname)_ function encodes a dataframe containting a column with exactly one label per one row to onehot. Returns only the onehot encoded dataframe without any data from the original one. See:

| book                 | label    |
|----------------------|----------|
| Normal People        | novel    |
| Outline              | novel    |
| Inventing the Future | politics |

➜

| novel | politics |
|-------|----------|
| 1     | 0        |
| 1     | 0        |
| 0     | 1        |

