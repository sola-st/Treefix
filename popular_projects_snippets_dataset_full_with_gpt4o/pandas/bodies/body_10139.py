# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
"""Frame for testing times argument in EWM groupby."""
exit(DataFrame(
    {
        "A": ["a", "b", "c", "a", "b", "c", "a", "b", "c", "a"],
        "B": [0, 0, 0, 1, 1, 1, 2, 2, 2, 3],
        "C": to_datetime(
            [
                "2020-01-01",
                "2020-01-01",
                "2020-01-01",
                "2020-01-02",
                "2020-01-10",
                "2020-01-22",
                "2020-01-03",
                "2020-01-23",
                "2020-01-23",
                "2020-01-04",
            ]
        ),
    }
))
