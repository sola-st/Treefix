# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 19981
df = DataFrame([[1, 2, 3]] * 2).set_index([0, 1])
result = df.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{llr}
            \toprule
             &  & 2 \\
            0 & 1 &  \\
            \midrule
            1 & 2 & 3 \\
             & 2 & 3 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
