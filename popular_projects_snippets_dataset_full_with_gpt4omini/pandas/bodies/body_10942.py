# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# Multiple groupby keys and as_index=False
gp = education_df.groupby(["country", "gender"], as_index=False, sort=False)
result = gp["education"].value_counts(
    normalize=normalize, sort=sort, ascending=ascending
)
expected = DataFrame()
for column in ["country", "gender", "education"]:
    expected[column] = [education_df[column][row] for row in expected_rows]
if normalize:
    expected["proportion"] = expected_count
    expected["proportion"] /= expected_group_size
else:
    expected["count"] = expected_count
tm.assert_frame_equal(result, expected)
