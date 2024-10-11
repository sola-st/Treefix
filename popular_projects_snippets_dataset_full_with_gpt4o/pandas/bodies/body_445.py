# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# npdev 2020-02-02 changed from "data type not understood" to
#  "Cannot interpret 'foo' as a data type"
msg = "|".join(
    ["data type not understood", "Cannot interpret '.*' as a data type"]
)
with pytest.raises(TypeError, match=msg):
    np.dtype(dtype)

assert not dtype == np.str_
assert not np.str_ == dtype
