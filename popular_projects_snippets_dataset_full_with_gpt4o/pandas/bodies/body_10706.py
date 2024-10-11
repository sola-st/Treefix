# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_missing.py
# GH 34725

df_without_nan_rows = DataFrame([(1, 0.1), (2, 0.2)])

ridx = [-1, 0, -1, -1, 1, -1]
df = df_without_nan_rows.reindex(ridx).reset_index(drop=True)

group_b = np.nan if has_nan_group else "b"
df["group_col"] = pd.Series(["a"] * 3 + [group_b] * 3)

grouped = df.groupby(by="group_col", dropna=dropna)
result = getattr(grouped, method)(limit=None)

expected_rows = {
    ("ffill", True, True): [-1, 0, 0, -1, -1, -1],
    ("ffill", True, False): [-1, 0, 0, -1, 1, 1],
    ("ffill", False, True): [-1, 0, 0, -1, 1, 1],
    ("ffill", False, False): [-1, 0, 0, -1, 1, 1],
    ("bfill", True, True): [0, 0, -1, -1, -1, -1],
    ("bfill", True, False): [0, 0, -1, 1, 1, -1],
    ("bfill", False, True): [0, 0, -1, 1, 1, -1],
    ("bfill", False, False): [0, 0, -1, 1, 1, -1],
}

ridx = expected_rows.get((method, dropna, has_nan_group))
expected = df_without_nan_rows.reindex(ridx).reset_index(drop=True)
# columns are a 'take' on df.columns, which are object dtype
expected.columns = expected.columns.astype(object)

tm.assert_frame_equal(result, expected)
