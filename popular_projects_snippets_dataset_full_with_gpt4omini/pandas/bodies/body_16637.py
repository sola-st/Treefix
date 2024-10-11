# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH 29864
index = pd.date_range("2019-10-01", freq="30min", periods=5, tz="UTC")
left = pd.DataFrame([0.9, 0.8, 0.7, 0.6], columns=["xyz"], index=index[1:])
right = pd.DataFrame({"from_date": index, "abc": [2.46] * 4 + [2.19]})
result = merge_asof(
    left=left, right=right, left_index=True, right_on=["from_date"]
)
expected = pd.DataFrame(
    {
        "xyz": [0.9, 0.8, 0.7, 0.6],
        "from_date": index[1:],
        "abc": [2.46] * 3 + [2.19],
    },
    index=pd.date_range(
        "2019-10-01 00:30:00", freq="30min", periods=4, tz="UTC"
    ),
)
tm.assert_frame_equal(result, expected)

result = merge_asof(
    left=right, right=left, right_index=True, left_on=["from_date"]
)
expected = pd.DataFrame(
    {
        "from_date": index,
        "abc": [2.46] * 4 + [2.19],
        "xyz": [np.nan, 0.9, 0.8, 0.7, 0.6],
    },
    index=Index([0, 1, 2, 3, 4]),
)
tm.assert_frame_equal(result, expected)
