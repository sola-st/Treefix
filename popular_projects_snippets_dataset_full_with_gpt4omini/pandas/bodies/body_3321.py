# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
# GH#32593
index = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
col1 = [5, 4, 3, 5, 8, 5, 2, 1, 6, 6]
col2 = [5, 4, np.nan, 5, 8, 5, np.inf, np.nan, 6, -np.inf]
df = DataFrame(
    data={
        "col1": col1,
        "col2": col2,
    },
    index=index,
    dtype="f8",
)
df_result = df.rank()

series_result = df.copy()
series_result["col1"] = df["col1"].rank()
series_result["col2"] = df["col2"].rank()

tm.assert_frame_equal(df_result, series_result)
