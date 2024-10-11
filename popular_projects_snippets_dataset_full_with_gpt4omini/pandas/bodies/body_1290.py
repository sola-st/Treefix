# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
# GH 4939, make sure to update the cache on setitem

df = tm.makeDataFrame()
df["A"]  # cache series
df.loc["Hello Friend"] = df.iloc[0]
assert "Hello Friend" in df["A"].index
assert "Hello Friend" in df["B"].index
