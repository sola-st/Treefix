# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
df = DataFrame({"A": [0, 1], "B": [1, 2], "C": [3, 4]})
result = df.groupby("A").agg(b=("B", lambda x: 0), c=("C", lambda x: 1))
expected = DataFrame({"b": [0, 0], "c": [1, 1]}, index=Index([0, 1], name="A"))
tm.assert_frame_equal(result, expected)
