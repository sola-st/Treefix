# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
# GH 35325
d = {"price": [10, 11, 9], "volume": [50, 60, 50]}

df = DataFrame(d)

df["week_starting"] = date_range("01/01/2018", periods=3, freq="W")

result = (
    df.set_index("week_starting")
    .groupby("volume")
    .resample("1D")
    .interpolate(method="linear")
)

expected_ind = pd.MultiIndex.from_tuples(
    [
        (50, Timestamp("2018-01-07")),
        (50, Timestamp("2018-01-08")),
        (50, Timestamp("2018-01-09")),
        (50, Timestamp("2018-01-10")),
        (50, Timestamp("2018-01-11")),
        (50, Timestamp("2018-01-12")),
        (50, Timestamp("2018-01-13")),
        (50, Timestamp("2018-01-14")),
        (50, Timestamp("2018-01-15")),
        (50, Timestamp("2018-01-16")),
        (50, Timestamp("2018-01-17")),
        (50, Timestamp("2018-01-18")),
        (50, Timestamp("2018-01-19")),
        (50, Timestamp("2018-01-20")),
        (50, Timestamp("2018-01-21")),
        (60, Timestamp("2018-01-14")),
    ],
    names=["volume", "week_starting"],
)

expected = DataFrame(
    data={
        "price": [
            10.0,
            9.928571428571429,
            9.857142857142858,
            9.785714285714286,
            9.714285714285714,
            9.642857142857142,
            9.571428571428571,
            9.5,
            9.428571428571429,
            9.357142857142858,
            9.285714285714286,
            9.214285714285714,
            9.142857142857142,
            9.071428571428571,
            9.0,
            11.0,
        ],
        "volume": [50.0] * 15 + [60],
    },
    index=expected_ind,
)
tm.assert_frame_equal(result, expected)
