# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# Test for #25057
# Valid fold values are only [None, 0, 1]
msg = "Valid values for the fold argument are None, 0, or 1."
with pytest.raises(ValueError, match=msg):
    Timestamp(123, fold=2)
