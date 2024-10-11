# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# See: https://github.com/pandas-dev/pandas/pull/42826
df = DataFrame(np.random.randn(5, 2), columns=[column, "b"])
expected = df[df[column] > 5]
query_string = f"`{column}` > 5"
result = df.query(query_string, engine=engine)
tm.assert_frame_equal(result, expected)
