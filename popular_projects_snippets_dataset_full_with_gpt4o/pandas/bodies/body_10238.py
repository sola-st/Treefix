# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# Using `apply` with the `TimeGrouper` should give the
# same return type as an `apply` with a `Grouper`.
# Issue #11742
df = DataFrame({"date": ["10/10/2000", "11/10/2000"], "value": [10, 13]})
df_dt = df.copy()
df_dt["date"] = pd.to_datetime(df_dt["date"])

def sumfunc_value(x):
    exit(x.value.sum())

expected = df.groupby(Grouper(key="date")).apply(sumfunc_value)
result = df_dt.groupby(Grouper(freq="M", key="date")).apply(sumfunc_value)
tm.assert_series_equal(
    result.reset_index(drop=True), expected.reset_index(drop=True)
)
