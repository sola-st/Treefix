# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
dates = [
    "2011-07-19 07:00:00",
    "2011-07-19 08:00:00",
    "2011-07-19 09:00:00",
    "2011-07-19 07:00:00",
    "2011-07-19 08:00:00",
    "2011-07-19 09:00:00",
]
df = DataFrame(
    {
        "label": ["a", "a", "a", "b", "b", "b"],
        "period": [pd.Period(d, freq="H") for d in dates],
        "value1": np.arange(6, dtype="int64"),
        "value2": [1, 2] * 3,
    }
)

exp_idx1 = pd.PeriodIndex(
    [
        "2011-07-19 07:00:00",
        "2011-07-19 07:00:00",
        "2011-07-19 08:00:00",
        "2011-07-19 08:00:00",
        "2011-07-19 09:00:00",
        "2011-07-19 09:00:00",
    ],
    freq="H",
    name="period",
)
exp_idx2 = Index(["a", "b"] * 3, name="label")
exp_idx = MultiIndex.from_arrays([exp_idx1, exp_idx2])
expected = DataFrame(
    {"value1": [0, 3, 1, 4, 2, 5], "value2": [1, 2, 2, 1, 1, 2]},
    index=exp_idx,
    columns=["value1", "value2"],
)

result = df.groupby(["period", "label"]).sum()
tm.assert_frame_equal(result, expected)

# by level
didx = pd.PeriodIndex(dates, freq="H")
df = DataFrame(
    {"value1": np.arange(6, dtype="int64"), "value2": [1, 2, 3, 1, 2, 3]},
    index=didx,
)

exp_idx = pd.PeriodIndex(
    ["2011-07-19 07:00:00", "2011-07-19 08:00:00", "2011-07-19 09:00:00"],
    freq="H",
)
expected = DataFrame(
    {"value1": [3, 5, 7], "value2": [2, 4, 6]},
    index=exp_idx,
    columns=["value1", "value2"],
)

result = df.groupby(level=0).sum()
tm.assert_frame_equal(result, expected)
