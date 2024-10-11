# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 14618
df = DataFrame(
    {
        "ColumnOk": [0.0, np.finfo(np.double).eps, 4.49423283715579e307],
        "ColumnTooBig": [0.0, np.finfo(np.double).eps, np.finfo(np.double).max],
    }
)
msg = (
    r"Column ColumnTooBig has a maximum value \(.+\) outside the range "
    r"supported by Stata \(.+\)"
)
with pytest.raises(ValueError, match=msg):
    with tm.ensure_clean() as path:
        df.to_stata(path)
