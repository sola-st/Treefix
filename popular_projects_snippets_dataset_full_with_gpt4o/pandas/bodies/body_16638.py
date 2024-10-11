# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# https://github.com/pandas-dev/pandas/issues/35558
dr1 = pd.date_range(start="1/1/2020", end="1/20/2020", freq="2D") + Timedelta(
    seconds=0.4
)
dr2 = pd.date_range(start="1/1/2020", end="2/1/2020")

df1 = pd.DataFrame({"val1": "foo"}, index=pd.DatetimeIndex(dr1))
df2 = pd.DataFrame({"val2": "bar"}, index=pd.DatetimeIndex(dr2))

expected = pd.DataFrame(
    {"val1": "foo", "val2": "bar"}, index=pd.DatetimeIndex(dr1)
)
result = merge_asof(
    df1,
    df2,
    left_index=True,
    right_index=True,
    tolerance=Timedelta(seconds=0.5),
)
tm.assert_frame_equal(result, expected)
