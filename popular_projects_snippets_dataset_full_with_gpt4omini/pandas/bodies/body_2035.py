# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# these will error
msg = "invalid unit abbreviation: foo"
with pytest.raises(ValueError, match=msg):
    to_timedelta(arg, unit="foo")
