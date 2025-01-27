# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#22035
df = DataFrame([[init_value, "str", "str2"]], columns=["a", "b", "b"])

# with the enforcement of GH#45333 in 2.0, this sets values inplace,
#  so we retain object dtype
df.iloc[:, 0] = df.iloc[:, 0].astype(dtypes)

expected_df = DataFrame(
    [[expected_value, "str", "str2"]],
    columns=["a", "b", "b"],
    dtype=object,
)
tm.assert_frame_equal(df, expected_df)
