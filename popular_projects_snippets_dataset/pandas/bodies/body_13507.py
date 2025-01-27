# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
s = Series(["a", "b", "c"])
result = s.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{ll}
            \toprule
             & 0 \\
            \midrule
            0 & a \\
            1 & b \\
            2 & c \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
