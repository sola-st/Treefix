# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_single_mgr("f8", num_rows=5)
assert mgr.external_values().tolist() == [0.0, 1.0, 2.0, 3.0, 4.0]
