# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_formats.py
# GH 32553

markers = Series(
    ["foo", "bar"],
    index=IntervalIndex(
        [
            Interval(left, right)
            for left, right in zip(
                Index([329.973, 345.137], dtype="float64"),
                Index([345.137, 360.191], dtype="float64"),
            )
        ]
    ),
)
result = str(markers)
expected = "(329.973, 345.137]    foo\n(345.137, 360.191]    bar\ndtype: object"
assert result == expected
