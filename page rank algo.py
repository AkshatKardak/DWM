## Page Rank
# PageRank Algorithm with user input for damping factor and convergence

# ---- User Input ----
nodes = input("Enter node names separated by space (e.g., A B C D): ").split()
n = len(nodes)
node_index = {nodes[i]: i for i in range(n)}

# Initialize adjacency matrix
adj_matrix = [[0] * n for _ in range(n)]

print("\nEnter outgoing links for each node (space-separated). Leave empty if no outgoing links.")
for node in nodes:
    links = input(f"Outgoing links from {node}: ").split()
    for link in links:
        if link not in node_index:
            print(f"Warning: {link} is not a valid node. Skipping.")
            continue
        adj_matrix[node_index[node]][node_index[link]] = 1

# Damping factor
while True:
    try:
        d = float(input("\nEnter damping factor (0-1, e.g., 0.85): "))
        if 0 < d < 1:
            break
        else:
            print("Please enter a number between 0 and 1.")
    except:
        print("Invalid input. Enter a decimal number between 0 and 1.")

epsilon = 0.0001  # convergence threshold
PR = [1 / n] * n  # initial PageRank values
out_degree = [sum(row) for row in adj_matrix]

# ---- PageRank Iterations ----
print("\nPageRank Iterations:\n")
print("Iteration\t" + "\t".join(nodes))

iteration = 0
while True:
    iteration += 1
    new_PR = [0] * n
    for i in range(n):
        rank_sum = 0
        for j in range(n):
            if adj_matrix[j][i] == 1 and out_degree[j] != 0:
                rank_sum += PR[j] / out_degree[j]
        new_PR[i] = (1 - d) / n + d * rank_sum

    # Print iteration table
    print(f"{iteration}\t\t" + "\t".join(f"{x:.4f}" for x in new_PR))

    # Check convergence
    if all(abs(new_PR[i] - PR[i]) < epsilon for i in range(n)):
        PR = new_PR
        break
    PR = new_PR

# ---- Final Ranking ----
ranking = sorted([(nodes[i], PR[i]) for i in range(n)], key=lambda x: x[1], reverse=True)

print("\nFinal Node Ranking:")
for node, _ in ranking:
    print(f"{node} -> ", end="")
print("END")

print("\nOrdered nodes by rank:", " -> ".join([node for node, _ in ranking]))

'''
Enter node names separated by space (e.g., A B C D): A B C D

Enter outgoing links for each node (space-separated). Leave empty if no outgoing links.
Outgoing links from A: B C
Outgoing links from B: C
Outgoing links from C: A
Outgoing links from D: C

Enter damping factor (0-1, e.g., 0.85): 0.85
'''