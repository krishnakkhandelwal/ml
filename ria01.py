import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 2. Load data (after using files.upload())
df = pd.read_csv("diabetes.csv")  # Use filename, not uploaded dict
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
display(df.head())
display(df.info())
display(df.describe())
# 3. Create independent (X) and dependent (y) variables
X = df.drop(columns=["Outcome"])  # Replace with your target col name
y = df["Outcome"]

# 4. Replace missing values (if any)
print(df.isnull().sum())
imputer = SimpleImputer(strategy="median")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# 5. Encoding categorical data (if any)
cat_cols = X.select_dtypes(include=['object']).columns
if len(cat_cols) > 0:
    X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

# 6. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
# 7. Feature scaling
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 9. EDA Plots
plt.figure(figsize=(5,4))
sns.countplot(x=y)
plt.title("Target Distribution")
plt.show()

df.hist(figsize=(12,10), bins=20)
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
