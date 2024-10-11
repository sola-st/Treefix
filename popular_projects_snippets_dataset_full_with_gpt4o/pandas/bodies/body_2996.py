# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py

# GH#14922: "sorting with large float and multiple columns incorrect"

# cause was that the int64 value NaT was considered as "na". Which is
# only correct for datetime64 columns.

int_values = (2, int(NaT.value))
float_values = (2.0, -1.797693e308)

df = DataFrame(
    {"int": int_values, "float": float_values}, columns=["int", "float"]
)

df_reversed = DataFrame(
    {"int": int_values[::-1], "float": float_values[::-1]},
    columns=["int", "float"],
    index=[1, 0],
)

# NaT is not a "na" for int64 columns, so na_position must not
# influence the result:
df_sorted = df.sort_values(["int", "float"], na_position="last")
tm.assert_frame_equal(df_sorted, df_reversed)

df_sorted = df.sort_values(["int", "float"], na_position="first")
tm.assert_frame_equal(df_sorted, df_reversed)

# reverse sorting order
df_sorted = df.sort_values(["int", "float"], ascending=False)
tm.assert_frame_equal(df_sorted, df)

# and now check if NaT is still considered as "na" for datetime64
# columns:
df = DataFrame(
    {"datetime": [Timestamp("2016-01-01"), NaT], "float": float_values},
    columns=["datetime", "float"],
)

df_reversed = DataFrame(
    {"datetime": [NaT, Timestamp("2016-01-01")], "float": float_values[::-1]},
    columns=["datetime", "float"],
    index=[1, 0],
)

df_sorted = df.sort_values(["datetime", "float"], na_position="first")
tm.assert_frame_equal(df_sorted, df_reversed)

df_sorted = df.sort_values(["datetime", "float"], na_position="last")
tm.assert_frame_equal(df_sorted, df)

# Ascending should not affect the results.
df_sorted = df.sort_values(["datetime", "float"], ascending=False)
tm.assert_frame_equal(df_sorted, df)
