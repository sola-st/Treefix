# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# gh 3016 (same as in update)
df = DataFrame(
    [[1.0, 2.0, False, True], [4.0, 5.0, True, False]],
    columns=["A", "B", "bool1", "bool2"],
)

other = DataFrame([[45, 45]], index=[0], columns=["A", "B"])
result = df.combine_first(other)
tm.assert_frame_equal(result, df)

df.loc[0, "A"] = np.nan
result = df.combine_first(other)
df.loc[0, "A"] = 45
tm.assert_frame_equal(result, df)
