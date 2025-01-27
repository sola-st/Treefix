# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
msg = "Could not convert 'foo' to NumPy timedelta"
with pytest.raises(ValueError, match=msg):
    to_timedelta(["foo", "bar"])
