# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
if data.fill_value == 0:
    # arith ops call on dtype.fill_value so that the sparsity
    # is maintained. Combine can't be called on a dtype in
    # general, so we can't make the expected. This is tested elsewhere
    pytest.skip("Incorrected expected from Series.combine and tested elsewhere")
