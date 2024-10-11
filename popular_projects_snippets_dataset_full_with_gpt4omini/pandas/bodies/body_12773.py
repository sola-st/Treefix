# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
recs = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "b": 5, "c": 6},
    {"a": 7, "b": 8, "c": 9},
    {"a": 10, "b": 11, "c": 12},
]

result = json_normalize(recs)
expected = DataFrame(recs)

tm.assert_frame_equal(result, expected)
