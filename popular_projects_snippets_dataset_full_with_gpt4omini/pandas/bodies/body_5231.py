# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# GH 24653: alias .to_numpy() for scalars
td = Timedelta("10m7s")
assert td.to_timedelta64() == td.to_numpy()

# GH#44460
msg = "dtype and copy arguments are ignored"
with pytest.raises(ValueError, match=msg):
    td.to_numpy("m8[s]")
with pytest.raises(ValueError, match=msg):
    td.to_numpy(copy=True)
