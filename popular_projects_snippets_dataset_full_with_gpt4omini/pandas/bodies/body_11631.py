# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# see gh-3795, gh-6607
parser = all_parsers

df = DataFrame(
    np.random.rand(5, 2).round(4),
    columns=list("AB"),
    index=["1A", "1B", "1C", "1D", "1E"],
)

with tm.ensure_clean("__passing_str_as_dtype__.csv") as path:
    df.to_csv(path)

    result = parser.read_csv(path, dtype=dtype, index_col=0)

    if check_orig:
        expected = df.copy()
        result = result.astype(float)
    else:
        expected = df.astype(str)

    tm.assert_frame_equal(result, expected)
