

import time
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, label_binarize
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
import numpy as np

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale for KNN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ===================== KNN MODEL =====================
# K value tuning
k_values = range(1, 16)
knn_scores = []
for k in k_values:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn_temp, X_train_scaled, y_train, cv=5)
    knn_scores.append(scores.mean())

best_k = k_values[np.argmax(knn_scores)]
print(f"Best K value from CV: {best_k}")

# Train final KNN model
start_time = time.time()
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train_scaled, y_train)
y_pred_knn = knn.predict(X_test_scaled)
knn_time = time.time() - start_time

# ===================== NAIVE BAYES MODEL =====================
start_time = time.time()
nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)
nb_time = time.time() - start_time

# ===================== METRICS =====================
print("\n--- Accuracy ---")
print(f"KNN Accuracy: {accuracy_score(y_test, y_pred_knn):.4f}")
print(f"Naive Bayes Accuracy: {accuracy_score(y_test, y_pred_nb):.4f}")

print("\n--- Classification Reports ---")
print("\nKNN:\n", classification_report(y_test, y_pred_knn, target_names=class_names))
print("Naive Bayes:\n", classification_report(y_test, y_pred_nb, target_names=class_names))

# Confusion Matrices
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.heatmap(confusion_matrix(y_test, y_pred_knn), annot=True, fmt="d", cmap="Blues",
            xticklabels=class_names, yticklabels=class_names, ax=axes[0])
axes[0].set_title("KNN Confusion Matrix")
axes[0].set_xlabel("Predicted")
axes[0].set_ylabel("Actual")

sns.heatmap(confusion_matrix(y_test, y_pred_nb), annot=True, fmt="d", cmap="Greens",
            xticklabels=class_names, yticklabels=class_names, ax=axes[1])
axes[1].set_title("Naive Bayes Confusion Matrix")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")
plt.tight_layout()
plt.show()

# Plot K value vs Accuracy
plt.figure(figsize=(6, 4))
plt.plot(k_values, knn_scores, marker='o', color='purple')
plt.title("K Value vs Accuracy")
plt.xlabel("Number of Neighbors (K)")
plt.ylabel("Cross-Validation Accuracy")
plt.grid(True)
plt.show()

# ===================== TIME COMPARISON =====================
print(f"\nTraining & Prediction Time:")
print(f"KNN: {knn_time:.6f} seconds")
print(f"Naive Bayes: {nb_time:.6f} seconds")