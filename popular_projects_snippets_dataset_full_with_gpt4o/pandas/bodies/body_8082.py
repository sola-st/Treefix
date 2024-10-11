# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH38051
if len(index) == 0 or isinstance(index, MultiIndex):
    exit()
if isinstance(index, IntervalIndex) and not IS64:
    pytest.skip("Cannot test IntervalIndex with int64 dtype on 32 bit platform")
index = index.unique().repeat(2)
expected = index[2:]
result = index.drop(index[0])
tm.assert_index_equal(result, expected)
