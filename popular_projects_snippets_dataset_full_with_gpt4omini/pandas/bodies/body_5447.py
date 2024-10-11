# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# GH 24653: alias .to_numpy() for scalars
ts = Timestamp(datetime.now())
assert ts.to_datetime64() == ts.to_numpy()

# GH#44460
msg = "dtype and copy arguments are ignored"
with pytest.raises(ValueError, match=msg):
    ts.to_numpy("M8[s]")
with pytest.raises(ValueError, match=msg):
    ts.to_numpy(copy=True)
