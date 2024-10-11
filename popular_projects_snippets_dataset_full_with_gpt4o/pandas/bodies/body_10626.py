# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
df = DataFrame({"A": [0, 0, 1, 1], "B": [1, 2, 3, 4]})
result = df.groupby("A").agg({"B": [lambda x: 0, lambda x: 1]})

expected = DataFrame(
    {("B", "<lambda_0>"): [0, 0], ("B", "<lambda_1>"): [1, 1]},
    index=Index([0, 1], name="A"),
)
tm.assert_frame_equal(result, expected)
