# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 14249
df = DataFrame({"a": [None, 1], "b": [2, 3], "c": [4, 5]})
if one_row:
    df = df.iloc[[0]]
observed = df.set_index(["a", "b"]).to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{llr}
            \toprule
             &  & c \\
            a & b &  \\
            \midrule
            NaN & 2 & 4 \\
            """
)
if not one_row:
    expected += r"""1.000000 & 3 & 5 \\
"""
expected += r"""\bottomrule
\end{tabular}
"""
assert observed == expected
