# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
f1 = lambda x, y, b=1: x.sum() + y + b
f2 = lambda x, y, b=2: x.sum() + y * b
result = Series([1, 2]).groupby([0, 0]).agg([f1, f2], 0)
expected = DataFrame({"<lambda_0>": [4], "<lambda_1>": [6]})
tm.assert_frame_equal(result, expected)

result = Series([1, 2]).groupby([0, 0]).agg([f1, f2], 0, b=10)
expected = DataFrame({"<lambda_0>": [13], "<lambda_1>": [30]})
tm.assert_frame_equal(result, expected)
