# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_coercion.py
# GH#12255
df = DataFrame(
    {
        0: np.array([1, 3], dtype=np.float32),
        1: np.array([2, 4], dtype=np.float32),
        2: ["a", "b"],
    }
)
orig = df.copy()

values = df[0].values.reshape(2, 1)
df.iloc[:, 0:1] = values

tm.assert_frame_equal(df, orig)
