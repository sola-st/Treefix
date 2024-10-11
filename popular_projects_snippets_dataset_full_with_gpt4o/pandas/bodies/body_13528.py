# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 25436
result = df_short.to_latex(caption=caption_table, label=label_table)
expected = _dedent(
    r"""
            \begin{table}
            \caption{a table in a \texttt{table/tabular} environment}
            \label{tab:table_tabular}
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
