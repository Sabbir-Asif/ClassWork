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

def generate_frequent_itemsets(initial_items, min_support, transactions, output_file):
    support_threshold = min_support

    item_support = calculate_item_support(initial_items, transactions)

    output_file.write("C1:\n")
    for item in item_support:
        output_file.write(f"[{item}]: {item_support[item]}\n")
    output_file.write("\n")

    frequent_itemsets = Counter()
    for item in item_support:
        if item_support[item] >= support_threshold:
            frequent_itemsets[frozenset([item])] += item_support[item]

    output_file.write("L1:\n")
    for itemset in frequent_itemsets:
        output_file.write(f"{list(itemset)}: {frequent_itemsets[itemset]}\n")
    output_file.write("\n")

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

        output_file.write(f"C{itemset_size}:\n")
        for candidate_set in item_support:
            output_file.write(f"{list(candidate_set)}: {item_support[candidate_set]}\n")
        output_file.write("\n")

        frequent_itemsets = Counter()
        for candidate_set in item_support:
            if item_support[candidate_set] >= support_threshold:
                frequent_itemsets[candidate_set] += item_support[candidate_set]

        output_file.write(f"L{itemset_size}:\n")
        for frequent_set in frequent_itemsets:
            output_file.write(f"{list(frequent_set)}: {frequent_itemsets[frequent_set]}\n")
        output_file.write("\n")

        if not frequent_itemsets:
            break

        previous_frequent_itemsets = frequent_itemsets
        position = itemset_size

    output_file.write("Result:\n")
    output_file.write(f"L{position}:\n")
    for frequent_set in previous_frequent_itemsets:
        output_file.write(f"{list(frequent_set)}: {previous_frequent_itemsets[frequent_set]}\n")
    output_file.write("\n")

    return previous_frequent_itemsets

def generate_association_rules(frequent_itemsets, transactions, output_file):
    result = []

    for itemset in frequent_itemsets:
        candidates = [frozenset(q) for q in combinations(itemset, len(itemset)-1)]
        max_confidence = 0
        for a in candidates:
            b = itemset - a
            ab = itemset
            support_ab = 0
            support_a = 0
            support_b = 0
            for transaction in transactions:
                transaction_set = set(transaction)
                if a.issubset(transaction_set):
                    support_a += 1
                if b.issubset(transaction_set):
                    support_b += 1
                if ab.issubset(transaction_set):
                    support_ab += 1
            confidence_a_b = support_ab / support_a * 100
            confidence_b_a = support_ab / support_b * 100
            result.append((list(a), list(b), confidence_a_b))
            result.append((list(b), list(a), confidence_b_a))

    output_file.write("Association Rules:\n")
    for combination in result:
        output_file.write(f"{combination[0]} -> {combination[1]} = {combination[2]:.2f}%\n")

# Example usage:
file_path = 'input500.txt'
out_path = 'output.txt'
min_support_count = 10

with open(out_path, 'w') as output_file:
    start_time = time.time()
    transactions_data = load_data(file_path)
    initial_items = set(item for transaction in transactions_data for item in transaction)
    frequent_itemsets_result = generate_frequent_itemsets(initial_items, min_support_count, transactions_data, output_file)
    generate_association_rules(frequent_itemsets_result, transactions_data, output_file)
    end_time = time.time()
    print(f"Execution time: {(end_time - start_time)}")

print("Execution complete.")
