import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\Joss\\Downloads\\Interactions Over Time.csv")
x = data['Pageviews Start']
y = data['Pageviews Pageviews']
data['Pageviews Pageviews'] = (
    data['Pageviews Pageviews']
    .str.replace(',', '')
    .astype(int)
)
y = data['Pageviews Pageviews']

print(y.max())
print(y.min())
print(y.mean())
