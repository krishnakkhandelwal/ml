# ML Assignment – 6
# Title: Clustering Techniques implementation and performance evaluation

# 1. Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, SpectralClustering, DBSCAN
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.decomposition import PCA

# 2. Load Dataset
iris = load_iris()
X = iris.data
y_true = iris.target

print("Shape of dataset:", X.shape)

# 3. Reduce dimensions for visualization (PCA -> 2D)
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)

# 4. Define models
models = {
    "KMeans": KMeans(n_clusters=3, random_state=42, n_init=10),
    "Spectral": SpectralClustering(n_clusters=3, affinity='nearest_neighbors',
                                   assign_labels='kmeans', random_state=42),
    "DBSCAN": DBSCAN(eps=0.5, min_samples=5)
}

# 5. Train models & evaluate
results = {}
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for i, (name, model) in enumerate(models.items()):
    labels = model.fit_predict(X)
    
    # Handle DBSCAN case (can produce -1 for noise points)
    if len(set(labels)) > 1:
        silhouette = silhouette_score(X, labels)
    else:
        silhouette = -1  # invalid silhouette if only 1 cluster
    
    ari = adjusted_rand_score(y_true, labels)
    
    results[name] = {
        "Silhouette Score": round(silhouette, 3),
        "ARI (vs true labels)": round(ari, 3),
        "Unique Clusters": len(set(labels))
    }
    
    # Visualization
    axes[i].scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', s=40)
    axes[i].set_title(f"{name} Clustering")

plt.suptitle("Clustering Visualization on Iris Dataset", fontsize=14)
plt.show()

# 6. Results Table
results_df = pd.DataFrame(results).T
print("\n=== Clustering Performance Results ===")
print(results_df)

# 7. Heatmap for quick comparison
plt.figure(figsize=(6, 4))
sns.heatmap(results_df.iloc[:, :2], annot=True, cmap="YlGnBu", fmt=".3f")
plt.title("Clustering Performance Comparison")
plt.show()
