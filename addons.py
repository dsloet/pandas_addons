from pandas.core.base import PandasObject

def select(df, column_name, value):
    """
    Intuitive way of applying filters to a dataframe

    Parameters
    ----------
    column_name : name of the columns
        column name for the function to be applied on.
    value : value to filter on
        value(s) to select within the column
    
    Returns
    -------
    dataframe with only the rows where the filter
    found a match


    """
    return df[df[column_name] == value]

PandasObject.select = select