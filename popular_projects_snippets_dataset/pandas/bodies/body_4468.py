# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH10056
data = [
    {"First": 1, "Second": 4, "Third": 7, "Fourth": 10},
    {"Second": 5, "First": 2, "Fourth": 11, "Third": 8},
    {"Second": 6, "First": 3, "Fourth": 12, "Third": 9, "YYY": 14, "XXX": 13},
]
expected = DataFrame(
    {
        "First": [1, 2, 3],
        "Second": [4, 5, 6],
        "Third": [7, 8, 9],
        "Fourth": [10, 11, 12],
        "YYY": [None, None, 14],
        "XXX": [None, None, 13],
    }
)
result = DataFrame(data)
tm.assert_frame_equal(result, expected)
