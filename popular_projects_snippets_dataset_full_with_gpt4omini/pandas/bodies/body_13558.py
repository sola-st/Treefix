# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 10660
df = DataFrame({"a": [0, 0, 1, 1], "b": list("abab"), "c": [1, 2, 3, 4]})
result = df.set_index(["a", "b"]).to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{llr}
            \toprule
             &  & c \\
            a & b &  \\
            \midrule
            0 & a & 1 \\
             & b & 2 \\
            1 & a & 3 \\
             & b & 4 \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
