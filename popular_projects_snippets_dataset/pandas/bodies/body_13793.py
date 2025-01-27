# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
result = df.style.applymap(lambda x: "color:baz;", subset=slice_)._compute().ctx
expected = {
    (r, c): [("color", "baz")]
    for r, row in enumerate(df.index)
    for c, col in enumerate(df.columns)
    if row in df.loc[slice_].index and col in df.loc[slice_].columns
}
assert result == expected
