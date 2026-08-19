# Ordinary Least Squares (OLS)

A common method used to find the best `m` and `b` is called **Ordinary Least Squares (OLS)**.

OLS tries to make the total squared prediction error as small as possible.

The objective is:

$$
\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
$$

Where:

* `yᵢ` → actual value
* `ŷᵢ` → predicted value
* `yᵢ - ŷᵢ` → prediction error
* `n` → number of training examples

The errors are squared so that positive and negative errors don't cancel each other out.

For example:

```text
Errors:

+2
-3
+5
```

Without squaring:

```text
2 - 3 + 5 = 4
```

With squaring:

```text
2² + (-3)² + 5²
= 4 + 9 + 25
= 38
```

OLS chooses the line that minimizes this squared-error value.

---

# The Complete Process

```text
Training Data
      ↓
Linear Regression
      ↓
Find the best m and b
      ↓
Create the best-fit line
      ↓
Use the line for predictions
```

In simple terms:

> **Linear Regression finds a line.**
>
> **OLS finds the best values for the line's parameters.**

---

# Multiple Features

The simple formula uses one feature:

$$
f(x) = mx + b
$$

But real ML problems usually have multiple features.

For example, house price might depend on:

```text
x₁ = house size
x₂ = number of bedrooms
x₃ = age of house
```

The model becomes:

$$
f(x) = b + w_1x_1 + w_2x_2 + w_3x_3
$$

More generally:

$$
f(x) = b + \sum_{j=1}^{n} w_jx_j
$$

Here:

* `x₁, x₂, ...` → features
* `w₁, w₂, ...` → weights/coefficient values
* `b` → intercept
* `f(x)` → predicted value

The idea is still the same:

**Find the coefficients that make the predictions fit the training data.**

---

# Scikit-Learn

In scikit-learn, linear regression can be implemented using:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)
```

After training:

```python
model.coef_
```

gives the learned coefficients (`m` or `w` values).

```python
model.intercept_
```

gives the learned intercept (`b`).

To make predictions:

```python
predictions = model.predict(X)
```

---

# Mental Model

Think of Linear Regression like this:

```text
             TRAINING
                ↓
        ┌────────────────┐
        │  Input X, y    │
        └───────┬────────┘
                ↓
        Find coefficients
          m / w₁ / w₂...
                +
              b
                ↓
        ┌────────────────┐
        │  Best-fit line │
        └───────┬────────┘
                ↓
             PREDICT
                ↓
          New X → ŷ
```

---

# Key Takeaways

* **Linear Regression** predicts continuous numerical values.

* The simplest form is:

  $$f(x) = mx + b$$

* `m` = slope / coefficient.

* `b` = intercept.

* During training, the model learns the best values for these parameters.

* **OLS (Ordinary Least Squares)** finds parameters by minimizing the sum of squared errors.

* After training, the model uses the learned equation to make predictions.

* With multiple features, the model becomes a weighted sum of the features.

### One-line summary

> **Linear Regression learns the best line from data so that it can predict new numerical values.**
