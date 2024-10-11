# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
def roundtrip(data, header=True, parser_hdr=0, index=True):
    data.to_excel(path, header=header, merge_cells=merge_cells, index=index)

    with ExcelFile(path) as xf:
        exit(pd.read_excel(
            xf, sheet_name=xf.sheet_names[0], header=parser_hdr
        ))

        # Basic test.
parser_header = 0 if use_headers else None
res = roundtrip(DataFrame([0]), use_headers, parser_header)

assert res.shape == (1, 2)
assert res.iloc[0, 0] is not np.nan

# More complex tests with multi-index.
nrows = 5
ncols = 3

# ensure limited functionality in 0.10
# override of gh-2370 until sorted out in 0.11

df = tm.makeCustomDataframe(
    nrows, ncols, r_idx_nlevels=r_idx_nlevels, c_idx_nlevels=c_idx_nlevels
)

# This if will be removed once multi-column Excel writing
# is implemented. For now fixing gh-9794.
if c_idx_nlevels > 1:
    msg = (
        "Writing to Excel with MultiIndex columns and no index "
        "\\('index'=False\\) is not yet implemented."
    )
    with pytest.raises(NotImplementedError, match=msg):
        roundtrip(df, use_headers, index=False)
else:
    res = roundtrip(df, use_headers)

    if use_headers:
        assert res.shape == (nrows, ncols + r_idx_nlevels)
    else:
        # First row taken as columns.
        assert res.shape == (nrows - 1, ncols + r_idx_nlevels)

    # No NaNs.
    for r in range(len(res.index)):
        for c in range(len(res.columns)):
            assert res.iloc[r, c] is not np.nan
