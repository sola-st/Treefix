# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_datetime.py
# GH#33589

keys = [
    "2017-10-25T16:25:04.151",
    "2017-10-25T16:25:04.252",
    "2017-10-25T16:50:05.237",
    "2017-10-25T16:50:05.238",
]
obj = frame_or_series(
    [1, 2, 3, 4],
    index=[Timestamp(x) for x in keys],
)
result = obj[keys[1] : keys[2]]
expected = frame_or_series(
    [2, 3],
    index=[
        Timestamp(keys[1]),
        Timestamp(keys[2]),
    ],
)
tm.assert_equal(result, expected)
