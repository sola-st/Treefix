# Extracted from https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them
list2 = [1, 2, 3, 4, 1, 2, 3]
lset = set()
[(lset.add(item), list2.append(item))
 for item in list2 if item not in lset]
print list(lset)

