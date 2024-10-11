# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_assign.py
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
original = df.copy()
result = df.assign(C=df.B / df.A)
expected = df.copy()
expected["C"] = [4, 2.5, 2]
tm.assert_frame_equal(result, expected)

# lambda syntax
result = df.assign(C=lambda x: x.B / x.A)
tm.assert_frame_equal(result, expected)

# original is unmodified
tm.assert_frame_equal(df, original)

# Non-Series array-like
result = df.assign(C=[4, 2.5, 2])
tm.assert_frame_equal(result, expected)
# original is unmodified
tm.assert_frame_equal(df, original)

result = df.assign(B=df.B / df.A)
expected = expected.drop("B", axis=1).rename(columns={"C": "B"})
tm.assert_frame_equal(result, expected)

# overwrite
result = df.assign(A=df.A + df.B)
expected = df.copy()
expected["A"] = [5, 7, 9]
tm.assert_frame_equal(result, expected)

# lambda
result = df.assign(A=lambda x: x.A + x.B)
tm.assert_frame_equal(result, expected)
