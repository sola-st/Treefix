# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# from the vb_suite/frame_methods/frame_insert_columns
N = 10
K = 5
df = DataFrame(index=range(N))
new_col = np.random.randn(N)
for i in range(K):
    df[i] = new_col
expected = DataFrame(np.repeat(new_col, K).reshape(N, K), index=range(N))
tm.assert_frame_equal(df, expected)
