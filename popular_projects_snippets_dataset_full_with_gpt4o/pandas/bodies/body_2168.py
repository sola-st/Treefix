# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# float
df = DataFrame({"year": [2000, 2001], "month": [1.5, 1], "day": [1, 1]})
msg = (
    r"^cannot assemble the datetimes: unconverted data remains: "
    r'"1", at position 0$'
)
with pytest.raises(ValueError, match=msg):
    to_datetime(df, cache=cache)
