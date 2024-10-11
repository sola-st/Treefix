# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_names.py
# GH9857
result = pd.DataFrame({"x": [1, 2, 6], "y": [2, 2, 8], "z": [-5, 0, 5]})
result = result.set_index("z")
result.loc[10] = [9, 10]
df_expected = pd.DataFrame(
    {"x": [1, 2, 6, 9], "y": [2, 2, 8, 10], "z": [-5, 0, 5, 10]}
)
df_expected = df_expected.set_index("z")
tm.assert_frame_equal(result, df_expected)
