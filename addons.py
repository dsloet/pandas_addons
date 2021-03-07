from pandas.core.base import PandasObject
import numpy as np


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


def median_abs_dev(df, axis=None, skipna=None):
    """
    Calculate the median absolute deviation of the variable X.
    Robust way of MAD when there are outliers in the data. Can be used in 
    combination with calcuting the robust z-score.

    Calculation of median absolute deviation:

    median_abs_dev = median{|xi - median(X)|}

    Parameters
    ----------
    axis : {axis_descr}
        Axis for the function to be applied on.
    skipna : bool, default None
        Exclude NA/null values when computing the result.

    Returns
    -------
    median absolute deviation of the Variable X

    """
    if skipna is None:
        skipna = True
    if axis is None:
        axis = df._stat_axis_number

    data = df._get_numeric_data()
    # print("median of the sample = ", data.median())
    if axis == 0:
        demedianed = data - data.median(axis=0)
    else:
        demedianed = data.sub(data.median(axis=1), axis=0)
    return np.abs(demedianed).median(axis=axis, skipna=skipna)


PandasObject.select = select
PandasObject.median_abs_dev = median_abs_dev