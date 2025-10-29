## Hierarchical Clustering
# ---- Hierarchical Clustering (Manual Implementation) ----
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram

# ---- Euclidean Distance ----
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# ---- Sample Data ----
points = np.array([
    [1, 1],
    [1.5, 1.5],
    [5, 5],
    [3, 4],
    [4.5, 4.5]
])
n = len(points)
k = 2  # Desired number of clusters

# ---- Manual Agglomerative Clustering (Single Linkage) ----
clusters = [[i] for i in range(n)]
cluster_ids = list(range(n))
next_cluster_id = n
merge_history = []  # entries: (left_id, right_id, distance, new_size)

while len(clusters) > 1:
    min_dist = float("inf")
    merge_i = merge_j = -1
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            dist = min(
                euclidean_distance(points[p1], points[p2])
                for p1 in clusters[i]
                for p2 in clusters[j]
            )
            if dist < min_dist:
                min_dist = dist
                merge_i, merge_j = i, j

    left_id = cluster_ids[merge_i]
    right_id = cluster_ids[merge_j]
    new_cluster = clusters[merge_i] + clusters[merge_j]
    new_size = len(new_cluster)
    merge_history.append((left_id, right_id, min_dist, new_size))

    # Remove merged clusters
    for idx in sorted([merge_i, merge_j], reverse=True):
        clusters.pop(idx)
        cluster_ids.pop(idx)

    # Add new cluster
    clusters.append(new_cluster)
    cluster_ids.append(next_cluster_id)
    next_cluster_id += 1

# ---- Derive labels for desired k ----
cluster_map = {i: [i] for i in range(n)}
current_set = set(range(n))
next_id = n
labels = [0] * n

for left_id, right_id, dist, size in merge_history:
    cluster_map[next_id] = cluster_map[left_id] + cluster_map[right_id]
    current_set.remove(left_id)
    current_set.remove(right_id)
    current_set.add(next_id)
    if len(current_set) == k:
        break
    next_id += 1

sorted_clusters = sorted(list(current_set), key=lambda cid: min(cluster_map[cid]))
for label_idx, cid in enumerate(sorted_clusters, start=1):
    for pt in cluster_map[cid]:
        labels[pt] = label_idx

# ---- Print Cluster Assignments ----
print("\nCluster assignments:")
for idx, lab in enumerate(labels, start=1):
    print(f"Point {idx} ({points[idx-1][0]}, {points[idx-1][1]}) -> Cluster {lab}")

# ---- Convert merge_history to linkage matrix for scipy dendrogram ----
Z = np.array(merge_history)

# ---- Plot dendrogram ----
plt.figure(figsize=(10, 6))
dendrogram(Z, labels=[f"P{i+1}" for i in range(n)], color_threshold=0)
plt.title("Dendrogram (Single-Linkage, Manual Calculation)")
plt.ylabel("Distance (Euclidean)")
plt.show()

# ---- Scatter plot showing final clusters ----
plt.figure(figsize=(6, 6))
colors = plt.cm.get_cmap('tab10')
for i in range(n):
    plt.scatter(points[i, 0], points[i, 1],
                color=colors((labels[i]-1) % 10),
                s=80, edgecolor='k')
    plt.text(points[i, 0]+0.05, points[i, 1]+0.05, f"P{i+1}", fontsize=9)
plt.title(f"Points colored by cluster (k={k})")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.show()



# Enter number of data points: 5
# Enter x y for point 1: 1 1
# Enter x y for point 2: 1.5 1.5
# Enter x y for point 3: 5 5
# Enter x y for point 4: 3 4
# Enter x y for point 5: 4.5 4.5
# Enter desired number of clusters: 2