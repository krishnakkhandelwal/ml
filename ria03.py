# Name : Krishna Khandelwal
# PRN  : 1032232078
# Roll : 50
# TY BTECH CSE AIDS (PANEL A)

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# ===================== Load Dataset =====================
df = pd.read_csv("data_dt.csv")

# ===================== Encode Non-Numeric Columns =====================
label_encoders = {}
for column in df.columns:
    if df[column].dtype == object:  # if column is categorical
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

# ===================== Split Features and Target =====================
X = df.iloc[:, :-1]   # all columns except last as features
y = df.iloc[:, -1]    # last column as target

# ===================== Train-Test Split =====================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===================== Decision Tree Model =====================
clf = DecisionTreeClassifier(criterion="entropy", random_state=42)
clf.fit(X_train, y_train)

# ===================== Predictions =====================
y_pred = clf.predict(X_test)

# ===================== Classification Report =====================
print("Classification Report:\n", classification_report(y_test, y_pred))

# ===================== Confusion Matrix =====================
plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred),
            annot=True, cmap='Blues', fmt='d',
            xticklabels=clf.classes_, yticklabels=clf.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Decision Tree Confusion Matrix")
plt.show()

# ===================== K-Fold Cross Validation =====================
scores = cross_val_score(clf, X, y, cv=5)
print("Cross-validation scores:", scores)
print("Average CV Accuracy:", scores.mean())

# ===================== Decision Tree Visualization =====================
plt.figure(figsize=(15,10))
plot_tree(clf, filled=True,
          feature_names=X.columns,
          class_names=[str(c) for c in clf.classes_])
plt.title("Decision Tree Visualization")
plt.show()
