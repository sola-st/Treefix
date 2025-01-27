# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH#27994
data = {"column_a": [5, 10], "column_b": ["one", "two"]}
index = [Timestamp("2021-01-01"), Timestamp("2021-01-01")]
df = DataFrame(data, index=index)

# Passing empty list-like should return the same DataFrame.
expected = df.copy()
result = df.drop(empty_listlike)
tm.assert_frame_equal(result, expected)
