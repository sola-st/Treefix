# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
special_characters = ["&", "%", "$", "#", "_", "{", "}", "~", "^", "\\"]
df = DataFrame(data=special_characters)
result = df.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{ll}
            \toprule
             & 0 \\
            \midrule
            0 & \& \\
            1 & \% \\
            2 & \$ \\
            3 & \# \\
            4 & \_ \\
            5 & \{ \\
            6 & \} \\
            7 & \textasciitilde  \\
            8 & \textasciicircum  \\
            9 & \textbackslash  \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
