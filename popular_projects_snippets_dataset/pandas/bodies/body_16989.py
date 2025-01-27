# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
"""48510 `concat` to an empty EA should maintain type EA dtype."""
df_empty = DataFrame({"a": pd.array([], dtype=pd.Int64Dtype())})
df_new = DataFrame({"a": pd.array([1, 2, 3], dtype=pd.Int64Dtype())})
expected = df_new.copy()
result = concat([df_empty, df_new])
tm.assert_frame_equal(result, expected)
