# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 18669
mi = pd.MultiIndex.from_product([[1, 2]], names=[""])
df = DataFrame(-1, index=mi, columns=range(4))
observed = df.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{lrrrr}
            \toprule
             & 0 & 1 & 2 & 3 \\
             &  &  &  &  \\
            \midrule
            1 & -1 & -1 & -1 & -1 \\
            2 & -1 & -1 & -1 & -1 \\
            \bottomrule
            \end{tabular}
            """
)
assert observed == expected
