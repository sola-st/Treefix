# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
first = index[5:20]
second = index[:10]
first.name = first_name
second.name = second_name
intersect = first.intersection(second, sort=sort)
assert intersect.name == expected_name
