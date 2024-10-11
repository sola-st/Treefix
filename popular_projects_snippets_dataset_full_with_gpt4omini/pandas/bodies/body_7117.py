# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# this is really a smoke test for the methods
# as these are adequately tested for function elsewhere
if len(index) == 0:
    tm.assert_numpy_array_equal(index.isna(), np.array([], dtype=bool))
elif isinstance(index, MultiIndex):
    idx = index.copy()
    msg = "isna is not defined for MultiIndex"
    with pytest.raises(NotImplementedError, match=msg):
        idx.isna()
elif not index.hasnans:
    tm.assert_numpy_array_equal(index.isna(), np.zeros(len(index), dtype=bool))
    tm.assert_numpy_array_equal(index.notna(), np.ones(len(index), dtype=bool))
else:
    result = isna(index)
    tm.assert_numpy_array_equal(index.isna(), result)
    tm.assert_numpy_array_equal(index.notna(), ~result)
