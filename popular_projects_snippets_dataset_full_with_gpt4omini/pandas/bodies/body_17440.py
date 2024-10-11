# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# check that offset._validate_n raises TypeError on a timedelt64
#  object
off = _create_offset(offset_types)

td64 = np.timedelta64(4567, "s")
with pytest.raises(TypeError, match="argument must be an integer"):
    type(off)(n=td64, **off.kwds)
