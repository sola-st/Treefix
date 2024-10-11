# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 16719
mi = pd.MultiIndex.from_product(
    [[0.0, 1.0], [3.0, 2.0, 1.0], ["0", "1"]], names=["i", "val0", "val1"]
)
df = DataFrame(index=mi)
result = df.to_latex(multirow=True, escape=False)
expected = _dedent(
    r"""
            \begin{tabular}{lll}
            \toprule
            i & val0 & val1 \\
            \midrule
            \multirow[t]{6}{*}{0.000000} & \multirow[t]{2}{*}{3.000000} & 0 \\
             &  & 1 \\
            \cline{2-3}
             & \multirow[t]{2}{*}{2.000000} & 0 \\
             &  & 1 \\
            \cline{2-3}
             & \multirow[t]{2}{*}{1.000000} & 0 \\
             &  & 1 \\
            \cline{1-3} \cline{2-3}
            \multirow[t]{6}{*}{1.000000} & \multirow[t]{2}{*}{3.000000} & 0 \\
             &  & 1 \\
            \cline{2-3}
             & \multirow[t]{2}{*}{2.000000} & 0 \\
             &  & 1 \\
            \cline{2-3}
             & \multirow[t]{2}{*}{1.000000} & 0 \\
             &  & 1 \\
            \cline{1-3} \cline{2-3}
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
