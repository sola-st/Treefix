# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 12031
df = DataFrame({"a": [1.0, 2.1], "b": ["b1", "b2"]})
result = df.to_latex(decimal=",")
expected = _dedent(
    r"""
            \begin{tabular}{lrl}
            \toprule
             & a & b \\
            \midrule
            0 & 1,000000 & b1 \\
            1 & 2,100000 & b2 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
