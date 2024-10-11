# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#43223
df = DataFrame(
    {"a": 0},
    index=DatetimeIndex(
        [
            "11.01.2011 22:00",
            "11.01.2011 23:00",
            "12.01.2011 00:00",
            "2011-01-13 00:00",
        ]
    ),
)
with pytest.raises(
    KeyError, match="Value based partial slicing on non-monotonic"
):
    df["2011-01-01":"2011-11-01"]
