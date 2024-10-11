# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
df = DataFrame(
    {
        "datetime64": [
            datetime(2016, 1, 1),
            datetime(2016, 2, 5),
            datetime(2016, 3, 3),
        ],
        "float": [1.0, 2.0, 3.0],
        "int": [1, 2, 3],
        "object": [(1, 2), True, False],
    }
)

formatters = {
    "datetime64": lambda x: x.strftime("%Y-%m"),
    "float": lambda x: f"[{x: 4.1f}]",
    "int": lambda x: f"0x{x:x}",
    "object": lambda x: f"-{x!s}-",
    "__index__": lambda x: f"index: {x}",
}
result = df.to_latex(formatters=dict(formatters))

expected = _dedent(
    r"""
            \begin{tabular}{llrrl}
            \toprule
             & datetime64 & float & int & object \\
            \midrule
            index: 0 & 2016-01 & [ 1.0] & 0x1 & -(1, 2)- \\
            index: 1 & 2016-02 & [ 2.0] & 0x2 & -True- \\
            index: 2 & 2016-03 & [ 3.0] & 0x3 & -False- \\
            \bottomrule
            \end{tabular}
            """
)
assert result == expected
