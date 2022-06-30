import numpy as np

def onehot(dataframe, labels_colname):
    """Encodes a dataframe containting a column
    with exactly one label per one row to onehot.
    Returns only the onehot encoded dataframe
    without any data from the original one.
    """
    labels=list(set(dataframe[labels_colname]))
    output=pd.DataFrame(np.zeros(shape=(len(dataframe), len(labels)),
                                    dtype="int"),
                        columns=labels)
    label_col=dataframe.columns.get_loc(labels_colname)+1
    for i, row in enumerate(dataframe.itertuples(), 0):
        output[row[label_col]][i]=1
    return output

