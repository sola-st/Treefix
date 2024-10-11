# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
if data.dtype == SparseDtype(int, 0):
    pytest.skip("Can't store nan in int array.")
