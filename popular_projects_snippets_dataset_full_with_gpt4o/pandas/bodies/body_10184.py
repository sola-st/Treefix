# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py

# GH 15130
# we don't need to validate monotonicity when grouping

# GH 43909 we should raise an error here to match
# behaviour of non-groupby rolling.

data = [
    ["David", "1/1/2015", 100],
    ["David", "1/5/2015", 500],
    ["David", "5/30/2015", 50],
    ["David", "7/25/2015", 50],
    ["Ryan", "1/4/2014", 100],
    ["Ryan", "1/19/2015", 500],
    ["Ryan", "3/31/2016", 50],
    ["Joe", "7/1/2015", 100],
    ["Joe", "9/9/2015", 500],
    ["Joe", "10/15/2015", 50],
]

df = DataFrame(data=data, columns=["name", "date", "amount"])
df["date"] = to_datetime(df["date"])
df = df.sort_values("date")

expected = (
    df.set_index("date")
    .groupby("name")
    .apply(lambda x: x.rolling("180D")["amount"].sum())
)
result = df.groupby("name").rolling("180D", on="date")["amount"].sum()
tm.assert_series_equal(result, expected)
