import pandas as pd
from addons import *

data = {
    "column1": ["foo", "bar", "bar", "foobar"],
    "column2": [1, 2, 3, 4],
    "column3": [1, np.nan, 500, 150000]
}

df = pd.DataFrame(data)


# print(df.select("column1", "bar"))

print(df["column2"].mad())
print(df["column2"].median_abs_dev())
print(df["column3"].mad())
print(df["column3"].median_abs_dev())
print(df["column3"].median_abs_dev(skipna=False))