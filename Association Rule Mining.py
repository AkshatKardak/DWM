# Associative rule mining
from itertools import combinations, chain

# ---- User Input ----
n = int(input("Enter number of transactions: "))
transactions = []
for i in range(n):
    items = input(f"Enter items for transaction {i+1} (space-separated): ").split()
    transactions.append(set(items))

min_support_count = int(input("Enter minimum support (number of transactions): "))
min_confidence_percent = float(input("Enter minimum confidence (percentage, e.g., 70): "))

# ---- Helper Functions ----
def generate_candidates(prev_frequent, k):
    """Generate candidate k-itemsets from previous frequent (k-1)-itemsets"""
    candidates = set()
    prev_list = list(prev_frequent)
    for i in range(len(prev_list)):
        for j in range(i + 1, len(prev_list)):
            union_set = prev_list[i] | prev_list[j]
            if len(union_set) == k:
                candidates.add(frozenset(union_set))
    return candidates

def calculate_support(transactions, candidates):
    """Calculate support count for each candidate"""
    support_count = {}
    for candidate in candidates:
        count = sum(1 for transaction in transactions if candidate.issubset(transaction))
        support_count[candidate] = count
    return support_count

# ---- Apriori Algorithm ----
frequent_itemsets = {}
k = 1

# Frequent 1-itemsets
all_items = set(chain.from_iterable(transactions))
candidates = [frozenset([item]) for item in all_items]
support_data = calculate_support(transactions, candidates)
Lk = {itemset: count for itemset, count in support_data.items() if count >= min_support_count}

while Lk:
    frequent_itemsets.update(Lk)
    k += 1
    candidates = generate_candidates(Lk.keys(), k)
    if not candidates:
        break
    support_data = calculate_support(transactions, candidates)
    Lk = {itemset: count for itemset, count in support_data.items() if count >= min_support_count}

# ---- Print Frequent Itemsets ----
if frequent_itemsets:
    print("\nFrequent Itemsets:")
    for itemset, count in sorted(frequent_itemsets.items(), key=lambda x: (-len(x[0]), -x[1])):
        print(f"{set(itemset)} -> support count: {count}")
else:
    print("\nNo frequent itemsets found with the given minimum support.")

# ---- Generate Association Rules ----
rules_found = False
print("\nAssociation Rules:")
for itemset in frequent_itemsets:
    if len(itemset) > 1:
        for i in range(1, len(itemset)):
            for antecedent in combinations(itemset, i):
                antecedent = frozenset(antecedent)
                consequent = itemset - antecedent
                conf = (frequent_itemsets[itemset] / frequent_itemsets[antecedent]) * 100
                if conf >= min_confidence_percent:
                    print(f"{set(antecedent)} => {set(consequent)} (confidence: {conf:.2f}%)")
                    rules_found = True

if not rules_found:
    print("No association rules found with the given confidence.")


# Enter number of transactions: 5
# Enter items for transaction 1 (space-separated): Milk Bread
# Enter items for transaction 2 (space-separated): Milk Diaper Beer Bread
# Enter items for transaction 3 (space-separated): Milk Diaper Beer Cola
# Enter items for transaction 4 (space-separated): Bread Milk Diaper Beer
# Enter items for transaction 5 (space-separated): Bread Milk Diaper Cola
# Enter minimum support (number of transactions): 3
# Enter minimum confidence (percentage, e.g., 70): 70