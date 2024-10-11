# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
index = float("nan")
table = table_type()
assert index not in table

table.set_item(index, 42)
assert len(table) == 1
assert index in table
assert table.get_item(index) == 42

table.set_item(index, 41)
assert len(table) == 1
assert index in table
assert table.get_item(index) == 41
