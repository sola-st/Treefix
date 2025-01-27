# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex_like.py
df = DataFrame({"x": list(range(5))})

result = df.reindex_like(df, method=method, tolerance=0)
tm.assert_frame_equal(df, result)
result = df.reindex_like(df, method=method, tolerance=[0, 0, 0, 0])
tm.assert_frame_equal(df, result)
