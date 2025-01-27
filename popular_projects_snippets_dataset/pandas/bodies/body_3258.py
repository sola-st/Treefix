# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#44417
vals = np.random.randn(3, 4)
df = DataFrame(vals, columns=["A", "B", "C", "A"])
dtypes = df.dtypes
dtypes.iloc[0] = str
dtypes.iloc[2] = "Float64"

result = df.astype(dtypes)
expected = DataFrame(
    {
        0: vals[:, 0].astype(str),
        1: vals[:, 1],
        2: pd.array(vals[:, 2], dtype="Float64"),
        3: vals[:, 3],
    }
)
expected.columns = df.columns
tm.assert_frame_equal(result, expected)
