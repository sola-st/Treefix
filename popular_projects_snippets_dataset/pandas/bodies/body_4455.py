# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
series = [Series(i, index=["b", "a", "c"], name=str(i)) for i in range(3)]
result = DataFrame(series)
expected = DataFrame(
    {"b": [0, 1, 2], "a": [0, 1, 2], "c": [0, 1, 2]},
    columns=["b", "a", "c"],
    index=["0", "1", "2"],
)
tm.assert_frame_equal(result, expected)
