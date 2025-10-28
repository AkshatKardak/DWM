##K-Means
import math

# Function to calculate Euclidean distance
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def kmeans():
    n = int(input("Enter number of data points: "))
    x, y = [], []
    print("Enter the coordinates (x y) for each point:")
    for _ in range(n):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)

    k = int(input("Enter number of clusters (k): "))

    # Initialize first k points as centroids
    centroidX = x[:k]
    centroidY = y[:k]
    cluster = [-1] * n

    # Repeat until convergence
    for iteration in range(100):
        changed = False

        # Step 1: Assign points to nearest centroid
        for i in range(n):
            minDist = distance(x[i], y[i], centroidX[0], centroidY[0])
            minCluster = 0
            for j in range(1, k):
                dist = distance(x[i], y[i], centroidX[j], centroidY[j])
                if dist < minDist:
                    minDist = dist
                    minCluster = j

            if cluster[i] != minCluster:
                cluster[i] = minCluster
                changed = True

        # Step 2: Update centroids
        newCentroidX = [0.0] * k
        newCentroidY = [0.0] * k
        count = [0] * k

        for i in range(n):
            newCentroidX[cluster[i]] += x[i]
            newCentroidY[cluster[i]] += y[i]
            count[cluster[i]] += 1

        for j in range(k):
            if count[j] > 0:
                centroidX[j] = newCentroidX[j] / count[j]
                centroidY[j] = newCentroidY[j] / count[j]

        # Print iteration result
        print(f"\nIteration {iteration + 1}:")
        for j in range(k):
            print(f" Centroid {j + 1}: ({centroidX[j]:.2f}, {centroidY[j]:.2f})")
        for i in range(n):
            print(f" Point ({x[i]:.2f}, {y[i]:.2f}) -> Cluster {cluster[i] + 1}")

        if not changed:
            break

    # Final Output
    print("\nFinal Clusters:")
    for j in range(k):
        print(f"Cluster {j + 1}: ", end="")
        for i in range(n):
            if cluster[i] == j:
                print(f"({x[i]:.2f}, {y[i]:.2f}) ", end="")
        print()

if __name__ == "__main__":
    kmeans()

# Enter number of data points: 6
# Enter the coordinates (x y) for each point:
# 1 1
# 1.5 2
# 3 4
# 5 7
# 3.5 5
# 4.5 5
# Enter number of clusters (k): 2