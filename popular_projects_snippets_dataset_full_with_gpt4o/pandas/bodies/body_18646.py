# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
table = table_type(1000)
state = table.get_state()
assert state["size"] == 0
assert state["n_occupied"] == 0
assert "n_buckets" in state
assert "upper_bound" in state
