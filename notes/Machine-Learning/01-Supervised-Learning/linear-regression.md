# Linear Regression

## What is Linear Regression?

**Linear Regression** is a supervised machine learning algorithm used to predict a **continuous numerical value**.

The basic idea is simple:

> Find a line that best describes the relationship between input `X` and output `y`.

For one feature, the line is written as:

$$
f(x) = mx + b
$$

Where:

* `x` → input feature
* `f(x)` → predicted output
* `m` → slope / coefficient
* `b` → intercept

---

## Simple Example

Suppose we want to predict a student's exam score based on how many hours they studied.

Our training data might look like:

| Hours Studied | Exam Score |
| ------------: | ---------: |
|             1 |         50 |
|             2 |         55 |
|             3 |         65 |
|             4 |         70 |
|             5 |         80 |

We want the model to learn a relationship between:

```text
X = Hours Studied
y = Exam Score
```

The model assumes a relationship like:

$$
f(x) = mx + b
$$

$$
Here, f(x) is pedicted value, m is the slope of the line and b is the intercept and x is the input.
$$

The values of `m` and `b` are **not chosen randomly by us**.

During training, the algorithm finds values of `m` and `b` that make the line fit the training data as well as possible.

---

# What are `m` and `b`?

Suppose the trained model finds:

$$
f(x) = 7x + 42
$$

Here:

```text
m = 7
b = 42
```

### `m` — Slope

`m` tells us how much the prediction changes when `x` increases by 1.

Here:

$$
m = 7
$$

So for every additional hour studied, the model predicts approximately **7 more marks**.

### `b` — Intercept

`b` is the predicted value when `x = 0`.

Here:

$$
b = 42
$$

So if a student studies 0 hours, the model predicts:

$$
f(0) = 7(0) + 42 = 42
$$

---

# Making a Prediction

Once the model has learned `m` and `b`, we can give it a new input.

Suppose:

```text
Hours studied = 6
```

The model is:

$$
f(x) = 7x + 42
$$

Therefore:

$$
f(6) = 7(6) + 42
$$

$$
f(6) = 84
$$

The model predicts an exam score of **84**.

---

# What Happens During Training?

This is the important part.

The model starts with the training data:

```text
Hours → Score

1 → 50
2 → 55
3 → 65
4 → 70
5 → 80
```

It tries to find the best values for:

```text
m → slope
b → intercept
```

This creates a line:

$$
\hat{y} = mx + b
$$

The model then compares its predictions with the actual values.

For example, suppose the model predicts:

```text
Actual score:    65
Predicted score: 63
```

The error is:

$$
65 - 63 = 2
$$

This difference is called the **residual** or **prediction error**.

