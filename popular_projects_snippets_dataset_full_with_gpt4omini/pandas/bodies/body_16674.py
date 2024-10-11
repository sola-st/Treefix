# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py

dt = datetime(2012, 5, 1)
dt2 = datetime(2012, 5, 2)
dt3 = datetime(2012, 5, 3)
dt4 = datetime(2012, 5, 4)

df1 = DataFrame({"x": ["a"]}, index=[dt])
df2 = DataFrame({"y": ["b", "c"]}, index=[dt, dt])
_check_merge(df1, df2)

# Not monotonic
df1 = DataFrame({"x": ["a", "b", "q"]}, index=[dt2, dt, dt4])
df2 = DataFrame(
    {"y": ["c", "d", "e", "f", "g", "h"]}, index=[dt3, dt3, dt2, dt2, dt, dt]
)
_check_merge(df1, df2)

df1 = DataFrame({"x": ["a", "b"]}, index=[dt, dt])
df2 = DataFrame({"y": ["c", "d"]}, index=[dt, dt])
_check_merge(df1, df2)
