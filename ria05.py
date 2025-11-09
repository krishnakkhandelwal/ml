# ML Assignment 5: Ensemble, Random Forest Classifier and Performance Measurement

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier, BaggingClassifier, AdaBoostClassifier,
    GradientBoostingClassifier, StackingClassifier
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve
)

# 1. Load dataset
data = pd.read_csv("diabetes.csv")
print("First 5 rows:\n", data.head())
print("\nDataset Info:\n")
print(data.info())
print("\nMissing values:\n", data.isnull().sum())

# 2. Features (X) and Target (y)
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# 3. Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)

# 5. Models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Bagging": BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=50, random_state=42),
    "AdaBoost": AdaBoostClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "Stacking": StackingClassifier(
        estimators=[
            ("rf", RandomForestClassifier(n_estimators=50, random_state=42)),
            ("dt", DecisionTreeClassifier(random_state=42)),
            ("ada", AdaBoostClassifier(random_state=42))
        ],
        final_estimator=LogisticRegression(),
        passthrough=True
    )
}

# 6. Train & Evaluate
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:,1])
    
    results[name] = acc
    print("\n=== {} ===".format(name))
    print("Accuracy:", acc)
    print("ROC-AUC:", roc_auc)
    print("Confusion Matrix:\n", cm)
    print("Classification Report:\n", report)

# 7. Compare Results
results_df = pd.DataFrame.from_dict(results, orient="index", columns=["Accuracy"])
print("\n=== Model Comparison ===")
print(results_df)

# 8. Plot Confusion Matrix (for best model)
best_model_name = results_df["Accuracy"].idxmax()
best_model = models[best_model_name]
y_best_pred = best_model.predict(X_test)
cm = confusion_matrix(y_test, y_best_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title(f"Confusion Matrix - {best_model_name}")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# 9. ROC Curves
plt.figure(figsize=(8,6))
for name, model in models.items():
    y_prob = model.predict_proba(X_test)[:,1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.plot(fpr, tpr, label=f"{name}")
    
plt.plot([0,1],[0,1],"k--")
plt.title("ROC Curves Comparison")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()
