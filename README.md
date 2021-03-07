# pandas_addons
Custom additions to pandas to make life easier


## filters available
### df.select(column_name, value)

Easy and more intuitive way of applying filters on a dataframe. Intention is
to minimize the typing.

### df.column_name.median_abs_dev()

Calculates MAD using the median instead of the mean. Robust way of calculating 
MAD when there are outliers in the data.