import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3, 4]})

def mult(data):
    data['a'] = 2
mult(df)
print(df)

print('yes')