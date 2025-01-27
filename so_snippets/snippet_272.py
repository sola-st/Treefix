# Extracted from https://stackoverflow.com/questions/1247486/list-comprehension-vs-map
def sum_items(*args):
    return sum(args)


list_a = [1, 2, 3]
list_b = [1, 2, 3]

list_of_sums = list(map(sum_items,
                        list_a, list_b))
[3, 6, 9]

comprehension = [sum(items) for items in iter(zip(list_a, list_b))]

def pair_list_items(*args):
    return args

packed_list = list(map(pair_list_items,
                       lista, *listb, listc.....listn))

