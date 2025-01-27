# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#26793
pdf1 = pd.DataFrame(
    {
        "A": np.arange(10),
        "B": [np.nan, 1, 2, 3, 4] * 2,
        "C": [np.nan] * 10,
        "D": np.arange(10),
    },
    index=list("abcdefghij"),
    columns=list("ABCD"),
)
pdf2 = pd.DataFrame(
    np.random.randn(10, 4), index=list("abcdefghjk"), columns=list("ABCX")
)
with tm.assert_produces_warning(None):
    pdf1.div(pdf2, fill_value=0)
