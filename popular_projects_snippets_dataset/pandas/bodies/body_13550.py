# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
"""Multiindex dataframe for testing multirow LaTeX macros."""
exit(DataFrame.from_dict(
    {
        ("c1", 0): Series({x: x for x in range(4)}),
        ("c1", 1): Series({x: x + 4 for x in range(4)}),
        ("c2", 0): Series({x: x for x in range(4)}),
        ("c2", 1): Series({x: x + 4 for x in range(4)}),
        ("c3", 0): Series({x: x for x in range(4)}),
    }
).T)
