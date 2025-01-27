# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# Test for #25057
# Check that we raise on fold conflict
msg = (
    "Cannot pass fold with possibly unambiguous input: int, float, "
    "numpy.datetime64, str, or timezone-aware datetime-like. "
    "Pass naive datetime-like or build Timestamp from components."
)
with pytest.raises(ValueError, match=msg):
    Timestamp(ts_input=ts_input, fold=fold)
