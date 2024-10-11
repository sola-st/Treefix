# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 42014
df = DataFrame([[1, 2], [3, 4]], index=["X", "Y"], columns=["X", "Y"])
idxs = ["X", "Y"] if index else ["Y"]
cols = ["X", "Y"] if columns else ["Y"]
df_styles = DataFrame("color: red;", index=idxs, columns=cols)
result = df.style.apply(lambda x: df_styles, axis=None)._compute().ctx

assert result[(1, 1)] == [("color", "red")]  # (Y,Y) styles always present
assert (result[(0, 1)] == [("color", "red")]) is index  # (X,Y) only if index
assert (result[(1, 0)] == [("color", "red")]) is columns  # (Y,X) only if cols
assert (result[(0, 0)] == [("color", "red")]) is (index and columns)  # (X,X)
