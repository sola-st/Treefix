# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# duplicates
msg = "cannot assemble with duplicate keys"
df2 = DataFrame({"year": [2015, 2016], "month": [2, 20], "day": [4, 5]})
df2.columns = ["year", "year", "day"]
with pytest.raises(ValueError, match=msg):
    to_datetime(df2, cache=cache)

df2 = DataFrame(
    {"year": [2015, 2016], "month": [2, 20], "day": [4, 5], "hour": [4, 5]}
)
df2.columns = ["year", "month", "day", "day"]
with pytest.raises(ValueError, match=msg):
    to_datetime(df2, cache=cache)
