# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
base_df = DataFrame({"A": [1, 1, 1, 1, 2, 2, 2, 2], "B": [np.nan] * 8})
base_df["B"] = base_df["B"].astype(dtype)
grouped = base_df.groupby("A")

expected = DataFrame({"B": [np.nan] * 8}, dtype=dtype)
result = getattr(grouped, method)()
tm.assert_frame_equal(expected, result)

result = getattr(grouped["B"], method)().to_frame()
tm.assert_frame_equal(expected, result)
