# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# #2538
start = datetime(2011, 1, 1, 5, 3, 40)
end = datetime(2011, 1, 1, 8, 9, 40)

msg = (
    "Of the four parameters: start, end, periods, and "
    "freq, exactly three must be specified"
)
with pytest.raises(ValueError, match=msg):
    date_range(start, end, periods=10, freq="s")
