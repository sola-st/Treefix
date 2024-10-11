# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
gr = Series([1, 2, 3, 4]).groupby([0, 0, 1, 1])
result = gr.agg([lambda x: 0, lambda x: 1])
exp_data = {"<lambda_0>": [0, 0], "<lambda_1>": [1, 1]}
expected = DataFrame(exp_data, index=np.array([0, 1]))
tm.assert_frame_equal(result, expected)
