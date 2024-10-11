# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_construct_from_scalar.py
td = np.timedelta64("NaT", "ns")
dt = np.datetime64("NaT", "ns")

with pytest.raises(TypeError, match="Cannot cast"):
    construct_1d_arraylike_from_scalar(td, 2, dt.dtype)

with pytest.raises(TypeError, match="Cannot cast"):
    construct_1d_arraylike_from_scalar(np.timedelta64(4, "ns"), 2, dt.dtype)

with pytest.raises(TypeError, match="Cannot cast"):
    construct_1d_arraylike_from_scalar(dt, 2, td.dtype)

with pytest.raises(TypeError, match="Cannot cast"):
    construct_1d_arraylike_from_scalar(np.datetime64(4, "ns"), 2, td.dtype)
