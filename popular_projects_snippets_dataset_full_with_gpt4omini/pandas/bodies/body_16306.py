# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# the dtype was being reset on the slicing and re-inferred to datetime
# even thought the blocks are mixed
belly = "216 3T19".split()
wing1 = "2T15 4H19".split()
wing2 = "416 4T20".split()
mat = pd.to_datetime("2016-01-22 2019-09-07".split())
df = DataFrame({"wing1": wing1, "wing2": wing2, "mat": mat}, index=belly)

result = df.loc["3T19"]
assert result.dtype == object
result = df.loc["216"]
assert result.dtype == object
