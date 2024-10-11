# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
the_position = "h"
df = DataFrame({"a": [1, 2], "b": ["b1", "b2"]})
result = df.to_latex(position=the_position)
expected = _dedent(
    r"""
            \begin{table}[h]
            \begin{tabular}{lrl}
            \toprule
             & a & b \\
            \midrule
            0 & 1 & b1 \\
            1 & 2 & b2 \\
            \bottomrule
            \end{tabular}
            \end{table}
            """
)
assert result == expected
