# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 28266
exp = DataFrame(
    {
        "B": [
            np.nan,
            np.nan,
            0.9999999999999998,
            -1.0,
            1.0,
            -0.3273268353539892,
            0.9999999999999998,
            1.0,
            0.9999999999999998,
            1.0,
        ],
        "A": [
            np.nan,
            np.nan,
            -1.0,
            1.0000000000000002,
            -0.3273268353539892,
            0.9999999999999966,
            1.0,
            1.0000000000000002,
            1.0,
            1.0000000000000002,
        ],
    },
    index=MultiIndex.from_tuples(
        [
            (Timestamp("20130101 09:00:00"), "B"),
            (Timestamp("20130101 09:00:00"), "A"),
            (Timestamp("20130102 09:00:02"), "B"),
            (Timestamp("20130102 09:00:02"), "A"),
            (Timestamp("20130103 09:00:03"), "B"),
            (Timestamp("20130103 09:00:03"), "A"),
            (Timestamp("20130105 09:00:05"), "B"),
            (Timestamp("20130105 09:00:05"), "A"),
            (Timestamp("20130106 09:00:06"), "B"),
            (Timestamp("20130106 09:00:06"), "A"),
        ]
    ),
)

df = DataFrame(
    {"B": [0, 1, 2, 4, 3], "A": [7, 4, 6, 9, 3]},
    index=[
        Timestamp("20130101 09:00:00"),
        Timestamp("20130102 09:00:02"),
        Timestamp("20130103 09:00:03"),
        Timestamp("20130105 09:00:05"),
        Timestamp("20130106 09:00:06"),
    ],
)

res = df.rolling(window="3d").corr()

tm.assert_frame_equal(exp, res)
