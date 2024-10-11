# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# min_periods no NAs (corner case)
expected = float_frame.cov()
result = float_frame.cov(min_periods=len(float_frame))

tm.assert_frame_equal(expected, result)

result = float_frame.cov(min_periods=len(float_frame) + 1)
assert isna(result.values).all()

# with NAs
frame = float_frame.copy()
frame.iloc[:5, frame.columns.get_loc("A")] = np.nan
frame.iloc[5:10, frame.columns.get_loc("B")] = np.nan
result = frame.cov(min_periods=len(frame) - 8)
expected = frame.cov()
expected.loc["A", "B"] = np.nan
expected.loc["B", "A"] = np.nan
tm.assert_frame_equal(result, expected)

# regular
result = frame.cov()
expected = frame["A"].cov(frame["C"])
tm.assert_almost_equal(result["A"]["C"], expected)

# fails on non-numeric types
with pytest.raises(ValueError, match="could not convert string to float"):
    float_string_frame.cov()
result = float_string_frame.cov(numeric_only=True)
expected = float_string_frame.loc[:, ["A", "B", "C", "D"]].cov()
tm.assert_frame_equal(result, expected)

# Single column frame
df = DataFrame(np.linspace(0.0, 1.0, 10))
result = df.cov()
expected = DataFrame(
    np.cov(df.values.T).reshape((1, 1)), index=df.columns, columns=df.columns
)
tm.assert_frame_equal(result, expected)
df.loc[0] = np.nan
result = df.cov()
expected = DataFrame(
    np.cov(df.values[1:].T).reshape((1, 1)),
    index=df.columns,
    columns=df.columns,
)
tm.assert_frame_equal(result, expected)
