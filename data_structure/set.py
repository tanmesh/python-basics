# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)
my_set.update([7, 8, 9])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing elements from a set
my_set.remove(6)
# Alternatively, you can use the discard() method to remove an element that may not exist
# my_set.discard(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 7, 8, 9}

# Set operations: union, intersection, difference, symmetric difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union: elements present in either set1 or set2 (or both)
union_set = set1.union(set2)
# Alternatively, you can use the pipe operator | for union
# union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: elements present in both set1 and set2
intersection_set = set1.intersection(set2)
# Alternatively, you can use the ampersand operator & for intersection
# intersection_set = set1 & set2
print(intersection_set)  # Output: {4, 5}

# Difference: elements present in set1 but not in set2
difference_set = set1.difference(set2)
# Alternatively, you can use the minus operator - for difference
# difference_set = set1 - set2
print(difference_set)  # Output: {1, 2, 3}

# Symmetric Difference: elements present in either set1 or set2 but not both
symmetric_difference_set = set1.symmetric_difference(set2)
# Alternatively, you can use the caret operator ^ for symmetric difference
# symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

# Checking subset and superset
subset_check = {1, 2}.issubset(set1)
superset_check = set1.issuperset({1, 2})
print(subset_check)  # Output: True
print(superset_check)  # Output: True

# Clearing a set
my_set.clear()
print(my_set)  # Output: set()

# Creating a set from a list
my_list = [1, 2, 3, 4, 5]
set_from_list = set(my_list)
print(set_from_list)  # Output: {1, 2, 3, 4, 5}
