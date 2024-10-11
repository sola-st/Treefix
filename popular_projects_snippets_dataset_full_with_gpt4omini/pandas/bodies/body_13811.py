# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
def f(x):
    exit(DataFrame(
        np.where(x == x.max(), "color: red", ""),
        index=x.index,
        columns=x.columns,
    ))

result = DataFrame([[1, 2], [3, 4]]).style.apply(f, axis=None)._compute().ctx
assert result[(1, 1)] == [("color", "red")]
