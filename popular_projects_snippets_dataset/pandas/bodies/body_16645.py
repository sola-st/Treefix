# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH#42844
right = pd.DataFrame(
    {
        "a": [2, 6],
        "ts": [pd.Timestamp("2021/01/01 00:37"), pd.Timestamp("2021/01/01 01:40")],
    }
)
ts_merge = pd.date_range(
    start=pd.Timestamp("2021/01/01 00:00"), periods=3, freq="1h"
)
left = pd.DataFrame({"b": [4, 8, 7]})
result = merge_asof(
    left,
    right,
    left_on=ts_merge,
    right_on="ts",
    allow_exact_matches=False,
    direction="backward",
)
expected = pd.DataFrame({"b": [4, 8, 7], "a": [np.nan, 2, 6], "ts": ts_merge})
tm.assert_frame_equal(result, expected)

result = merge_asof(
    right,
    left,
    left_on="ts",
    right_on=ts_merge,
    allow_exact_matches=False,
    direction="backward",
)
expected = pd.DataFrame(
    {
        "a": [2, 6],
        "ts": [pd.Timestamp("2021/01/01 00:37"), pd.Timestamp("2021/01/01 01:40")],
        "b": [4, 8],
    }
)
tm.assert_frame_equal(result, expected)
