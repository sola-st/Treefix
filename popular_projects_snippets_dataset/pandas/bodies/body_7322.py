# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_formats.py
# GH#9116
idx1 = TimedeltaIndex([], freq="D")
idx2 = TimedeltaIndex(["1 days"], freq="D")
idx3 = TimedeltaIndex(["1 days", "2 days"], freq="D")
idx4 = TimedeltaIndex(["1 days", "2 days", "3 days"], freq="D")
idx5 = TimedeltaIndex(["1 days 00:00:01", "2 days", "3 days"])

exp1 = "TimedeltaIndex: 0 entries\nFreq: D"

exp2 = "TimedeltaIndex: 1 entries, 1 days to 1 days\nFreq: D"

exp3 = "TimedeltaIndex: 2 entries, 1 days to 2 days\nFreq: D"

exp4 = "TimedeltaIndex: 3 entries, 1 days to 3 days\nFreq: D"

exp5 = "TimedeltaIndex: 3 entries, 1 days 00:00:01 to 3 days 00:00:00"

for idx, expected in zip(
    [idx1, idx2, idx3, idx4, idx5], [exp1, exp2, exp3, exp4, exp5]
):
    result = idx._summary()
    assert result == expected
