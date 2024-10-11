# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH#40024
ser = Series([1000.0, "test"])
result = ser.to_latex(float_format="{:,.0f}".format)
expected = _dedent(
    r"""
            \begin{tabular}{ll}
            \toprule
             & 0 \\
            \midrule
            0 & 1,000 \\
            1 & test \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
