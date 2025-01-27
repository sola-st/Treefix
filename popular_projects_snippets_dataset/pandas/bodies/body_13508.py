# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 18326
df = DataFrame({"a": [1, 2]})
df.index.name = "foo"
result = df.to_latex(index_names=False)
expected = _dedent(
    r"""
            \begin{tabular}{lr}
            \toprule
             & a \\
            \midrule
            0 & 1 \\
            1 & 2 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
