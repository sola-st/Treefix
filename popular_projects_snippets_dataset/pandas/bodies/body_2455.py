# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#47381
df = DataFrame(columns=["a", "b"])
expected = df.copy()
view = df[:]
with tm.assert_produces_warning(None):
    df.iloc[:, 0] = np.array([1, 2], dtype=np.float64)
tm.assert_frame_equal(view, expected)
