# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py

# systematically test the slicing operations:
#  for all slicing ops:
#   - returning a dataframe
#   - returning a column
#   - returning a row
#   - returning a single value

cats = Categorical(
    ["a", "c", "b", "c", "c", "c", "c"], categories=["a", "b", "c"]
)
idx = Index(["h", "i", "j", "k", "l", "m", "n"])
values = [1, 2, 3, 4, 5, 6, 7]
df = DataFrame({"cats": cats, "values": values}, index=idx)

# the expected values
cats2 = Categorical(["b", "c"], categories=["a", "b", "c"])
idx2 = Index(["j", "k"])
values2 = [3, 4]

# 2:4,: | "j":"k",:
exp_df = DataFrame({"cats": cats2, "values": values2}, index=idx2)

# :,"cats" | :,0
exp_col = Series(cats, index=idx, name="cats")

# "j",: | 2,:
exp_row = Series(["b", 3], index=["cats", "values"], dtype="object", name="j")

# "j","cats | 2,0
exp_val = "b"

# iloc
# frame
res_df = df.iloc[2:4, :]
tm.assert_frame_equal(res_df, exp_df)
assert is_categorical_dtype(res_df["cats"].dtype)

# row
res_row = df.iloc[2, :]
tm.assert_series_equal(res_row, exp_row)
assert isinstance(res_row["cats"], str)

# col
res_col = df.iloc[:, 0]
tm.assert_series_equal(res_col, exp_col)
assert is_categorical_dtype(res_col.dtype)

# single value
res_val = df.iloc[2, 0]
assert res_val == exp_val

# loc
# frame
res_df = df.loc["j":"k", :]
tm.assert_frame_equal(res_df, exp_df)
assert is_categorical_dtype(res_df["cats"].dtype)

# row
res_row = df.loc["j", :]
tm.assert_series_equal(res_row, exp_row)
assert isinstance(res_row["cats"], str)

# col
res_col = df.loc[:, "cats"]
tm.assert_series_equal(res_col, exp_col)
assert is_categorical_dtype(res_col.dtype)

# single value
res_val = df.loc["j", "cats"]
assert res_val == exp_val

# single value
res_val = df.loc["j", df.columns[0]]
assert res_val == exp_val

# iat
res_val = df.iat[2, 0]
assert res_val == exp_val

# at
res_val = df.at["j", "cats"]
assert res_val == exp_val

# fancy indexing
exp_fancy = df.iloc[[2]]

res_fancy = df[df["cats"] == "b"]
tm.assert_frame_equal(res_fancy, exp_fancy)
res_fancy = df[df["values"] == 3]
tm.assert_frame_equal(res_fancy, exp_fancy)

# get_value
res_val = df.at["j", "cats"]
assert res_val == exp_val

# i : int, slice, or sequence of integers
res_row = df.iloc[2]
tm.assert_series_equal(res_row, exp_row)
assert isinstance(res_row["cats"], str)

res_df = df.iloc[slice(2, 4)]
tm.assert_frame_equal(res_df, exp_df)
assert is_categorical_dtype(res_df["cats"].dtype)

res_df = df.iloc[[2, 3]]
tm.assert_frame_equal(res_df, exp_df)
assert is_categorical_dtype(res_df["cats"].dtype)

res_col = df.iloc[:, 0]
tm.assert_series_equal(res_col, exp_col)
assert is_categorical_dtype(res_col.dtype)

res_df = df.iloc[:, slice(0, 2)]
tm.assert_frame_equal(res_df, df)
assert is_categorical_dtype(res_df["cats"].dtype)

res_df = df.iloc[:, [0, 1]]
tm.assert_frame_equal(res_df, df)
assert is_categorical_dtype(res_df["cats"].dtype)
