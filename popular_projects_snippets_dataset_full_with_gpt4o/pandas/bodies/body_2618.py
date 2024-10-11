# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
# https://github.com/pandas-dev/pandas/issues/35521

# create non-consolidated dataframe with object dtype columns
df = DataFrame()
df["col1"] = Series(["a"], dtype=object)
df["col2"] = Series([0], dtype=object)

# access column (item cache)
df["col1"] == "A"
# take operation
# (regression was that this consolidated but didn't reset item cache,
# resulting in an invalid cache and the .at operation not working properly)
df[df["col2"] == 0]

# now setting value should update actual dataframe
df.at[0, "col1"] = "A"

expected = DataFrame({"col1": ["A"], "col2": [0]}, dtype=object)
tm.assert_frame_equal(df, expected)
assert df.at[0, "col1"] == "A"
