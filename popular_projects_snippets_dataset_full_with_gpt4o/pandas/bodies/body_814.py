# Extracted from ./data/repos/pandas/pandas/tests/internals/test_managers.py

with pd.option_context("mode.data_manager", "block"):
    s_block = pd.Series([1, 2, 3], name="A", index=["a", "b", "c"])
assert isinstance(s_block._mgr, SingleBlockManager)

with pd.option_context("mode.data_manager", "array"):
    s_array = pd.Series([1, 2, 3], name="A", index=["a", "b", "c"])
assert isinstance(s_array._mgr, SingleArrayManager)

# also ensure both are seen as equal
tm.assert_series_equal(s_block, s_array)

# conversion from one manager to the other
result = s_block._as_manager("block")
assert isinstance(result._mgr, SingleBlockManager)
result = s_block._as_manager("array")
assert isinstance(result._mgr, SingleArrayManager)
tm.assert_series_equal(result, s_block)

result = s_array._as_manager("array")
assert isinstance(result._mgr, SingleArrayManager)
result = s_array._as_manager("block")
assert isinstance(result._mgr, SingleBlockManager)
tm.assert_series_equal(result, s_array)
