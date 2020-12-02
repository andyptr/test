import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3, 4]})

def mult(data):
    return data * 2

df = mult(df)
df*3
print(df)

