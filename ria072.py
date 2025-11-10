# Assignment 7: Linear & Multiple Linear Regression Implementation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# -------------------- SINGLE LINEAR REGRESSION --------------------
# Custom dataset
np.random.seed(42)
X = np.linspace(5, 25, 25) + np.random.normal(0, 2, 25)
y = 3*X + 8 + np.random.normal(0, 8, 25)

# Reshape for sklearn
X = X.reshape(-1, 1)

# ---------- Split into Train/Test ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# ---------- Model Training ----------
model = LinearRegression()
model.fit(X_train, y_train)

# ---------- Prediction ----------
y_pred = model.predict(X_test)

# ---------- Output ----------
print("----- SINGLE LINEAR REGRESSION -----")
print("Coefficient (Slope):", model.coef_[0])
print("Intercept:", model.intercept_)

# ---------- Plot ----------
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
print("R-squared Score (R2):", metrics.r2_score(y_test, y_pred))


# -------------------- MULTIPLE LINEAR REGRESSION --------------------
# Create a synthetic dataset with 2 features
np.random.seed(42)
X_multi = np.random.rand(100, 2) * 10  # Two independent variables
y_multi = 5 + 2*X_multi[:,0] + 3*X_multi[:,1] + np.random.normal(0, 2, 100)  # Linear relation with noise

# ---------- Split into Train/Test ----------
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y_multi, test_size=0.2, random_state=10)

# ---------- Model Training ----------
multi_model = LinearRegression()
multi_model.fit(X_train_m, y_train_m)

# ---------- Prediction ----------
y_pred_m = multi_model.predict(X_test_m)

# ---------- Output ----------
print("\n----- MULTIPLE LINEAR REGRESSION -----")
print("Coefficients (Slopes):", multi_model.coef_)
print("Intercept:", multi_model.intercept_)

# ---------- Metrics ----------
print("Mean Absolute Error (MAE):", metrics.mean_absolute_error(y_test_m, y_pred_m))
print("Mean Squared Error (MSE):", metrics.mean_squared_error(y_test_m, y_pred_m))
print("Root Mean Squared Error (RMSE):", np.sqrt(metrics.mean_squared_error(y_test_m, y_pred_m)))
print("R-squared Score (R2):", metrics.r2_score(y_test_m, y_pred_m))

# ---------- Optional Visualization ----------
# For visualization (since we have 2 features), use a 3D plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_test_m[:,0], X_test_m[:,1], y_test_m, color='orange', label='Actual')
ax.scatter(X_test_m[:,0], X_test_m[:,1], y_pred_m, color='blue', label='Predicted')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Target')
ax.set_title('Multiple Linear Regression: Actual vs Predicted')
ax.legend()
plt.show()
