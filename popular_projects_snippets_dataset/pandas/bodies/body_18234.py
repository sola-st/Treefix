# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# Test for issue #10181
frames = [
    pd.DataFrame(dtype=dtype),
    pd.DataFrame(columns=["A"], dtype=dtype),
    pd.DataFrame(index=[0], dtype=dtype),
]
for df in frames:
    assert (df + df).equals(df)
    tm.assert_frame_equal(df + df, df)
