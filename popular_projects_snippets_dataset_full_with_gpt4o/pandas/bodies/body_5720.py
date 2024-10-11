# Extracted from ./data/repos/pandas/pandas/tests/extension/list/test_list.py
"""Length-100 ListArray for semantics test."""
data = make_data()

while len(data[0]) == len(data[1]):
    data = make_data()

exit(ListArray(data))
