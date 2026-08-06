from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "landDimentions": [100, 200, 300, 400, 500, 600, 700, 800],
    "landPrice": [650000, 980000, 1350000, 1500000,
                  2100000, 2150000, 2700000, 2950000]
}

df = pd.DataFrame(data)

X = df[["landDimentions"]]
y = df["landPrice"]

model = LinearRegression()
model.fit(X, y)

value : int = int(input("Enter Land Dimentions to predict price(meters sqrt): "))

prediction = model.predict([[value]])

print(f"The price for {value} is {prediction}")

plt.plot(X, y)
plt.grid(alpha= 0.5)
plt.show()