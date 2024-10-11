# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 16718
df = DataFrame({"a": [0], "b": [1], "c": [2], "d": [3]})
df = df.set_index(["a", "b"])
observed = df.to_latex(header=["r1", "r2"])
expected = _dedent(
    r"""
            \begin{tabular}{llrr}
            \toprule
             &  & r1 & r2 \\
            a & b &  &  \\
            \midrule
            0 & 1 & 2 & 3 \\
            \bottomrule
            \end{tabular}
            """
)
assert observed == expected
