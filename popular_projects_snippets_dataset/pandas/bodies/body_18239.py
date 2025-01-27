# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
box = Series if holder is Series else Index

if holder is RangeIndex:
    if dtype != np.int64:
        pytest.skip(f"dtype {dtype} not relevant for RangeIndex")
    idx = RangeIndex(0, 5, name="foo")
else:
    idx = holder(np.arange(5, dtype=dtype), name="foo")
result = np.sin(idx)
expected = box(np.sin(np.arange(5, dtype=dtype)), name="foo")
tm.assert_equal(result, expected)
