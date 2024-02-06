from collections import Counter
from itertools import combinations
import time 

def load_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    transactions = [line.strip().split()[1:] for line in lines]
    return transactions

def calculate_item_support(initial_items, transactions):
    item_counts = Counter()
    for item in initial_items:
        for transaction in transactions:
            if item in transaction:
                item_counts[item] += 1
    return item_counts

def generate_frequent_itemsets(initial_items, min_support, transactions):
    support_threshold = min_support

    item_support = calculate_item_support(initial_items, transactions)

    print("C1:")
    for item in item_support:
        print(f"[{item}]: {item_support[item]}")
    print()

    frequent_itemsets = Counter()
    for item in item_support:
        if item_support[item] >= support_threshold:
            frequent_itemsets[frozenset([item])] += item_support[item]

    print("L1:")
    for itemset in frequent_itemsets:
        print(f"{list(itemset)}: {frequent_itemsets[itemset]}")
    print()

    previous_frequent_itemsets = frequent_itemsets
    position = 1

    for itemset_size in range(2, 1000):
        new_candidates = set()
        previous_frequent_list = list(previous_frequent_itemsets)
        for i in range(len(previous_frequent_list)):
            for j in range(i+1, len(previous_frequent_list)):
                new_candidate_set = previous_frequent_list[i].union(previous_frequent_list[j])
                if len(new_candidate_set) == itemset_size:
                    new_candidates.add(previous_frequent_list[i].union(previous_frequent_list[j]))

        new_candidates = list(new_candidates)
        item_support = Counter()
        for candidate_set in new_candidates:
            item_support[candidate_set] = 0
            for transaction in transactions:
                transaction_set = set(transaction)
                if candidate_set.issubset(transaction_set):
                    item_support[candidate_set] += 1

        print(f"C{itemset_size}:")
        for candidate_set in item_support:
            print(f"{list(candidate_set)}: {item_support[candidate_set]}")
        print()

        frequent_itemsets = Counter()
        for candidate_set in item_support:
            if item_support[candidate_set] >= support_threshold:
                frequent_itemsets[candidate_set] += item_support[candidate_set]

        print(f"L{itemset_size}:")
        for frequent_set in frequent_itemsets:
            print(f"{list(frequent_set)}: {frequent_itemsets[frequent_set]}")
        print()

        if not frequent_itemsets:
            break

        previous_frequent_itemsets = frequent_itemsets
        position = itemset_size

    print("Result:")
    print(f"L{position}:")
    for frequent_set in previous_frequent_itemsets:
        print(f"{list(frequent_set)}: {previous_frequent_itemsets[frequent_set]}")
    print()

    return previous_frequent_itemsets

# Example usage:
file_path = 'input500.txt'
out_path = 'output.txt'
min_support_count = 10  #int(input("Enter minimum support count: "))

start_time = time.time()
transactions_data = load_data(file_path)
initial_items = set(item for transaction in transactions_data for item in transaction)
frequent_itemsets_result = generate_frequent_itemsets(initial_items, min_support_count, transactions_data)
end_time = time.time()

print('execution complete')
print(f"execution time : : {abs(start_time - end_time)}")