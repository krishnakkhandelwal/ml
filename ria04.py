# Assignment 04: SVM vs Decision Tree Classifier

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, mean_squared_error

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target





# Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ----- SVM Classifier -----
svm_clf = SVC(kernel='linear')
svm_clf.fit(X_train, y_train)
y_pred_svm = svm_clf.predict(X_test)

# Performance of SVM
acc_svm = accuracy_score(y_test, y_pred_svm)
mse_svm = mean_squared_error(y_test, y_pred_svm)

# ----- Decision Tree Classifier -----
dt_clf = DecisionTreeClassifier(random_state=42)
dt_clf.fit(X_train, y_train)
y_pred_dt = dt_clf.predict(X_test)
# Performance of Decision Tree
acc_dt = accuracy_score(y_test, y_pred_dt)
mse_dt = mean_squared_error(y_test, y_pred_dt)

# Print Results
print("SVM Accuracy:", acc_svm)
print("SVM Mean Squared Error:", mse_svm)
print("Decision Tree Accuracy:", acc_dt)
print("Decision Tree Mean Squared Error:", mse_dt)

# ----- Comparison Visualization -----
metrics = ['Accuracy', 'Mean Squared Error']
svm_scores = [acc_svm, mse_svm]
dt_scores = [acc_dt, mse_dt]

x = np.arange(len(metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(7,5))
bars1 = ax.bar(x - width/2, svm_scores, width, label='SVM')
bars2 = ax.bar(x + width/2, dt_scores, width, label='Decision Tree')

ax.set_ylabel('Score')
ax.set_title('Comparison of SVM and Decision Tree')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

# Adding values on top of bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.3f}', 
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')

plt.show()