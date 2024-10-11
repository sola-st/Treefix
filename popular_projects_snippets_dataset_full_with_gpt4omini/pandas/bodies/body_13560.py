# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# see gh-14484
#
# If an index is repeated in subsequent rows, it should be
# replaced with a blank in the created table. This should
# ONLY happen if all higher order indices (to the left) are
# equal too. In this test, 'c' has to be printed both times
# because the higher order index 'A' != 'B'.
df = DataFrame(
    index=pd.MultiIndex.from_tuples([("A", "c"), ("B", "c")]), columns=["col"]
)
result = df.to_latex()
expected = _dedent(
    r"""
            \begin{tabular}{lll}
            \toprule
             &  & col \\
            \midrule
            A & c & NaN \\
            B & c & NaN \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
