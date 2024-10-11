# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#12513
array_dim2 = np.arange(10).reshape((5, 2))
df = DataFrame(array_dim2, dtype="datetime64[ns, UTC]")

expected = DataFrame(array_dim2).astype("datetime64[ns, UTC]")
tm.assert_frame_equal(df, expected)
