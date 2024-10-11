# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
# see gh-9425
#
# Only supports freq up to WOM-4.
msg = (
    "Of the four parameters: start, end, periods, "
    "and freq, exactly three must be specified"
)

with pytest.raises(ValueError, match=msg):
    date_range("2014-01-01", freq="WOM-5MON")
