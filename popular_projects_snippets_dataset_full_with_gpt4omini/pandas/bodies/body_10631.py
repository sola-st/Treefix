# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH 33439
df = DataFrame({"A": ["S", "W", "W"], "B": [1.0, 1.0, 2.0]})
res = df.groupby("A").agg({"B": lambda x: x.get(x.index[-1])})
expected = DataFrame({"A": ["S", "W"], "B": [1.0, 2.0]}).set_index("A")
tm.assert_frame_equal(res, expected)
