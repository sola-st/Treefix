# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
df = DataFrame([r"a\b\c", r"^a^b^c", r"~a~b~c"])
result = df.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{ll}
            \toprule
             & 0 \\
            \midrule
            0 & a\textbackslash b\textbackslash c \\
            1 & \textasciicircum a\textasciicircum b\textasciicircum c \\
            2 & \textasciitilde a\textasciitilde b\textasciitilde c \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
