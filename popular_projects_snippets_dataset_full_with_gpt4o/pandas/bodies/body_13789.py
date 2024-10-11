# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 42014
df = DataFrame([[1, 2], [3, 4]], index=["X", "Y"], columns=["X", "Y"])

# test Series return where len(Series) < df.index or df.columns but labels OK
func = lambda s: Series(["color: red;"], index=["Y"])
result = df.style.apply(func, axis=axis)._compute().ctx
assert result[(1, 1)] == [("color", "red")]
assert result[(1 - axis, axis)] == [("color", "red")]

# test Series return where labels align but different order
func = lambda s: Series(["color: red;", "color: blue;"], index=["Y", "X"])
result = df.style.apply(func, axis=axis)._compute().ctx
assert result[(0, 0)] == [("color", "blue")]
assert result[(1, 1)] == [("color", "red")]
assert result[(1 - axis, axis)] == [("color", "red")]
assert result[(axis, 1 - axis)] == [("color", "blue")]
