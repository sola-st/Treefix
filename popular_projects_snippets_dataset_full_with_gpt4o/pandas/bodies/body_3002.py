# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH 13230
expected = DataFrame(
    {
        "A": [1, 2, 3, 4, 4],
        "date": pd.DatetimeIndex(
            [
                "2010-01-01 09:00:00",
                "2010-01-01 09:00:01",
                "2010-01-01 09:00:02",
                "2010-01-01 09:00:03",
                "NaT",
            ]
        ),
    }
)
result = expected.sort_values(["A", "date"])
tm.assert_frame_equal(result, expected)
