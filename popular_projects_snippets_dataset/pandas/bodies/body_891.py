# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
values = np.array([1.0, 2.0])
placement = slice(2)
msg = r"Wrong number of dimensions. values.ndim != ndim \[1 != 2\]"

with pytest.raises(ValueError, match=msg):
    block_maker(values, placement, ndim=2)
