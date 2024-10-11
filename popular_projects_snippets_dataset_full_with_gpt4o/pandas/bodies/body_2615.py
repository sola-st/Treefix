# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
# Ensure that PandasArray isn't allowed inside Series
# See https://github.com/pandas-dev/pandas/issues/23995 for more.
arr = Series([1, 2, 3]).array
result = DataFrame({"A": arr})
expected = DataFrame({"A": [1, 2, 3]})
tm.assert_frame_equal(result, expected)
assert isinstance(result._mgr.blocks[0], NumericBlock)
