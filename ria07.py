# Assignment 7: Linear Regression Implementation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn import metrics


# custom dataset
np.random.seed(42)
X = np.linspace(5, 25, 25) + np.random.normal(0, 2, 25)
y = 3*X + 8 + np.random.normal(0, 8, 25)

# Convert to 2D shape for sklearn
X = X.reshape(-1, 1)

# ---------- Split into Train/Test ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# ---------- Model Training ----------
model = LinearRegression()
model.fit(X_train, y_train)

# ---------- Prediction ----------
y_pred = model.predict(X_test)

# ---------- Output ----------
print("Model Coefficient (Slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)

# ---------- Plots ----------
plt.figure(figsize=(8,5))
plt.scatter(X_train, y_train, color='blue', label='Training Points')
plt.scatter(X_test, y_test, color='orange', label='Validation Points')
plt.plot(X, model.predict(X), color='green', label='Regression Line')
plt.xlabel('X (feature)')
plt.ylabel('y (target)')
plt.title('Linear Regression Fit and Validation')
plt.legend()
plt.grid(True)
plt.show()

# ---------- Metrics ----------
print("Mean Absolute Error (MAE):", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error (MSE):", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error (RMSE):", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print("R-squared Score (R²):", metrics.r2_score(y_test, y_pred))


