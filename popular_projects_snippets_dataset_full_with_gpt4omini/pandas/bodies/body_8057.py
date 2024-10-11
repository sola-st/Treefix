# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# DatetimeIndex is excluded, because it overrides getitem and should
# be tested separately.
empty_farr = np.array([], dtype=np.float_)
empty_index = type(index)([])

assert index[[]].identical(empty_index)
# np.ndarray only accepts ndarray of int & bool dtypes, so should Index
msg = r"arrays used as indices must be of integer \(or boolean\) type"
with pytest.raises(IndexError, match=msg):
    index[empty_farr]
