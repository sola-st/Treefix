# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# 8/6/12 is a Monday
ind = date_range(start="8/6/2012", end="8/26/2012", freq="D")
n = len(ind)
data = [[x] * 5 for x in range(n)]
df = DataFrame(data, columns=["open", "high", "low", "close", "vol"], index=ind)

# it works!
df.resample("W-MON", closed="left", label="left").first()
