# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
nan1 = (float("nan"),)
nan2 = (float("nan"),)
assert nan1[0] is not nan2[0]
table = ht.PyObjectHashTable()
table.set_item(nan1, 42)
assert table.get_item(nan2) == 42
