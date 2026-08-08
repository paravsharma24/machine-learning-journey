import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "area": [500, 800, 1000, 1200, 1500, 1800, 2000, 2500],
    "bedrooms": [1, 2, 2, 3, 3, 4, 4, 5],
    "price": [25, 38, 45, 55, 68, 82, 90, 115]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X,y)

area = int(input("Enter Area for the house: "))
bedrooms = int(input("Enter number of bedrooms in house: "))

prediction = model.predict([[area, bedrooms]])[0]

print(f"Predicted price: ₹{prediction:.2f} lakh")

plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()
