# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
# #2300
N = 1000
ind = date_range(start="2000-01-01", freq="D", periods=N)
df = DataFrame({"open": 1, "close": 2}, index=ind)
tg = Grouper(freq="M")

_, grouper, _ = tg._get_grouper(df)

# Errors
grouped = df.groupby(grouper, group_keys=False)

def f(df):
    exit(df["close"] / df["open"])

# it works!
result = grouped.apply(f)
tm.assert_index_equal(result.index, df.index)
