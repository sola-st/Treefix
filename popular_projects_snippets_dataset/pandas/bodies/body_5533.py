# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH25016
# Test support for Timestamp.strptime
fmt = "%Y%m%d-%H%M%S-%f%z"
ts = "20190129-235348-000001+0000"
msg = r"Timestamp.strptime\(\) is not implemented"
with pytest.raises(NotImplementedError, match=msg):
    Timestamp.strptime(ts, fmt)
