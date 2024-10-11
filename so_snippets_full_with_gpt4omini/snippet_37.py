# Extracted from https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend
x = [20]
# List passed to the append(object) method is treated as a single object.
x.append([21, 22, 23])
# Hence the resultant list length will be 2
print(x)
--> [20, [21, 22, 23]]

x = [20]
# The parameter passed to extend(list) method is treated as a list.
# Eventually it is two lists being concatenated.
x.extend([21, 22, 23])
# Here the resultant list's length is 4
print(x)
--> [20, 21, 22, 23]

