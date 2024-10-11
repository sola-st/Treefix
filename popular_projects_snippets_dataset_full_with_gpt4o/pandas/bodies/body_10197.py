# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 40951
halflife = "23 days"
# GH#42738
times = times_frame.pop("C")
result = times_frame.groupby("A").ewm(halflife=halflife, times=times).mean()
expected = DataFrame(
    {
        "B": [
            0.0,
            0.507534,
            1.020088,
            1.537661,
            0.0,
            0.567395,
            1.221209,
            0.0,
            0.653141,
            1.195003,
        ]
    },
    index=MultiIndex.from_tuples(
        [
            ("a", 0),
            ("a", 3),
            ("a", 6),
            ("a", 9),
            ("b", 1),
            ("b", 4),
            ("b", 7),
            ("c", 2),
            ("c", 5),
            ("c", 8),
        ],
        names=["A", None],
    ),
)
tm.assert_frame_equal(result, expected)
