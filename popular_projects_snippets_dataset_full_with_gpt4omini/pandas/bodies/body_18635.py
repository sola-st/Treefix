# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
index = 5
table = table_type(55)
assert len(table) == 0
assert index not in table

table.set_item(index, 42)
assert len(table) == 1
assert index in table
assert table.get_item(index) == 42

table.set_item(index + 1, 41)
assert index in table
assert index + 1 in table
assert len(table) == 2
assert table.get_item(index) == 42
assert table.get_item(index + 1) == 41

table.set_item(index, 21)
assert index in table
assert index + 1 in table
assert len(table) == 2
assert table.get_item(index) == 21
assert table.get_item(index + 1) == 41
assert index + 2 not in table

table.set_item(index + 1, 21)
assert index in table
assert index + 1 in table
assert len(table) == 2
assert table.get_item(index) == 21
assert table.get_item(index + 1) == 21

with pytest.raises(KeyError, match=str(index + 2)):
    table.get_item(index + 2)
