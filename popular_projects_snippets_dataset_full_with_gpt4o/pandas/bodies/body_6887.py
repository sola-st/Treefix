# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
if isinstance(index, PeriodIndex) and not IS64:
    pytest.skip("Overflow")
idx = index
assert idx.T.equals(idx)
assert idx.transpose().equals(idx)

values = idx.values

assert idx.shape == values.shape
assert idx.ndim == values.ndim
assert idx.size == values.size

if not isinstance(index, (RangeIndex, MultiIndex)):
    # These two are not backed by an ndarray
    assert idx.nbytes == values.nbytes

# test for validity
idx.nbytes
idx.values.nbytes
