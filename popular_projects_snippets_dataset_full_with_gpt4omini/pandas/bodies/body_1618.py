# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# gh-14836
df = DataFrame(np.random.rand(3, 3), columns=columns, index=list("ABC"))
expected = df.iloc[:, expected_columns]
result = df.loc[["A", "B", "C"], column_key]

tm.assert_frame_equal(result, expected, check_column_type=True)
