# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
with pytest.raises(ValueError, match=INVALID_FREQ_ERR_MSG):
    _get_offset("gibberish")
with pytest.raises(ValueError, match=INVALID_FREQ_ERR_MSG):
    _get_offset("QS-JAN-B")

pairs = [
    ("B", BDay()),
    ("b", BDay()),
    ("bm", BMonthEnd()),
    ("Bm", BMonthEnd()),
    ("W-MON", Week(weekday=0)),
    ("W-TUE", Week(weekday=1)),
    ("W-WED", Week(weekday=2)),
    ("W-THU", Week(weekday=3)),
    ("W-FRI", Week(weekday=4)),
]

for name, expected in pairs:
    offset = _get_offset(name)
    assert offset == expected, (
        f"Expected {repr(name)} to yield {repr(expected)} "
        f"(actual: {repr(offset)})"
    )
