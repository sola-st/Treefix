# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
# GH#27910
arr = SparseArray([0, 1], fill_value=0)

result = arr * np.array(2)
expected = arr * 2
tm.assert_sp_array_equal(result, expected)
