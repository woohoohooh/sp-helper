import pandas as pd   #  pip install pandas

columns=['Date', 'Model', 'Mark']

data = [
['2019-02-26', 'CE255X', 'nv print'],
['2019-02-26', 'CE255X', 'nv print'],
['2019-02-26', 'CE255X', 'nv print'],
['2019-02-26', 'CE255X', 'nv print']
]

df = pd.DataFrame(data, columns=columns)
df.to_csv(r'1cartridge_accounting.csv')