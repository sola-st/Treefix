# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
def h(x, color="bar"):
    exit(Series(f"color: {color}", index=x.index, name=x.name))

result = df.style.apply(h, axis=axis, subset=slice_, color="baz")._compute().ctx
expected = {
    (r, c): [("color", "baz")]
    for r, row in enumerate(df.index)
    for c, col in enumerate(df.columns)
    if row in df.loc[slice_].index and col in df.loc[slice_].columns
}
assert result == expected
