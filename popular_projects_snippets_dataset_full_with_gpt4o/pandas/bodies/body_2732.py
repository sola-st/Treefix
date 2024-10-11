# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# GH#32535 dont less tz in to_records
df = DataFrame({"A": date_range("2012-01-01", "2012-01-02", tz="US/Eastern")})

result = df.to_records()

assert result.dtype["A"] == object
val = result[0][1]
assert isinstance(val, Timestamp)
assert val == df.loc[0, "A"]
