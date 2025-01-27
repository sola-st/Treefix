# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py

# bad value for errors parameter
msg = "errors must be one of"
with pytest.raises(ValueError, match=msg):
    to_timedelta(["foo"], errors="never")
