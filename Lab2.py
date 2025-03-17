import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv("C:\\Users\\Joss\\Downloads\\Interactions by Category.csv")

# Clean the data
data['Pageviews By Course Category Sum Pageviews'] = (
    data['Pageviews By Course Category Sum Pageviews']
    .str.replace(',', '')
    .astype(int)
)

# Define the variables
x = data['Pageviews By Course Category Category'].values.reshape(-1, 1)
y = data['Pageviews By Course Category Sum Pageviews']

# Print statistics
print(y.max())
print(y.min())
print(y.mean())

# Create and fit the model
model = LinearRegression()
model.fit(x, y)

# Predict values
y_pred = model.predict(x)

# Plot the data
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_pred, color='red', label='Linear Regression')
plt.xlabel('Pageviews By Course Category Category')
plt.ylabel('Pageviews By Course Category Sum Pageviews')
plt.title('Pageviews By Course Category')
plt.legend()
plt.show()