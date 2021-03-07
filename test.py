import pandas as pd
from addons import *

data = {
    "column1":["foo", "bar", "bar"],
    "column2":[1, 2, 3]
}

df = pd.DataFrame(data)

print(df.select("column1", "bar"))