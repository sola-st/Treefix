# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# test that two chars caption is handled correctly
# it must not be unpacked into long_caption, short_caption.
result = df_short.to_latex(caption="xy")
expected = _dedent(
    r"""
            \begin{table}
            \caption{xy}
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
