# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
the_position = "t"
df = DataFrame({"a": [1, 2], "b": ["b1", "b2"]})
result = df.to_latex(longtable=True, position=the_position)
expected = _dedent(
    r"""
            \begin{longtable}[t]{lrl}
            \toprule
             & a & b \\
            \midrule
            \endfirsthead
            \toprule
             & a & b \\
            \midrule
            \endhead
            \midrule
            \multicolumn{3}{r}{Continued on next page} \\
            \midrule
            \endfoot
            \bottomrule
            \endlastfoot
            0 & 1 & b1 \\
            1 & 2 & b2 \\
            \end{longtable}
            """
)
assert result == expected
