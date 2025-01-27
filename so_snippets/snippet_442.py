# Extracted from https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list
pip install avemedi_lib

from avemedi_lib.functions import average, get_median, get_median_custom


test_even_array = [12, 32, 23, 43, 14, 44, 123, 15]
test_odd_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Getting average value of list items
print(average(test_even_array))  # 38.25

# Getting median value for ordered or unordered numbers list
print(get_median(test_even_array))  # 27.5
print(get_median(test_odd_array))  # 27.5

# You can use your own sorted and your count functions
a = sorted(test_even_array)
n = len(a)

print(get_median_custom(a, n))  # 27.5

