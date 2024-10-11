# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
df = DataFrame({0: ["Hello", "goodbye"], 1: [0, 1]})

result = df.sort_values(0, key=lambda col: col.str.lower())
expected = df[::-1]
tm.assert_frame_equal(result, expected)

result = df.sort_values(1, key=lambda col: -col)
expected = df[::-1]
tm.assert_frame_equal(result, expected)
