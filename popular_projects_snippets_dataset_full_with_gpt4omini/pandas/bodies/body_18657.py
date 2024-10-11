# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
nan1 = complex(float("nan"), 1)
nan2 = complex(float("nan"), 1)
other = complex(float("nan"), 2)
assert nan1 is not nan2
table = ht.PyObjectHashTable()
table.set_item(nan1, 42)
assert table.get_item(nan2) == 42
with pytest.raises(KeyError, match=None) as error:
    table.get_item(other)
assert str(error.value) == str(other)
