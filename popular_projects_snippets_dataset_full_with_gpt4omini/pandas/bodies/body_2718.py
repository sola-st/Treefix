# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_select_dtypes.py
# GH#42452
dtype_dict = {"A": float, "B": np.float64, "C": np.float32}
df = DataFrame(
    {"A": range(3), "B": range(5, 8), "C": range(10, 7, -1)},
)
df = df.astype(dtype_dict)
result = df.select_dtypes(include=float_dtypes)
tm.assert_frame_equal(result, expected)
