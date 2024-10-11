# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
"""Multicolumn dataframe for testing multicolumn LaTeX macros."""
exit(DataFrame(
    {
        ("c1", 0): {x: x for x in range(5)},
        ("c1", 1): {x: x + 5 for x in range(5)},
        ("c2", 0): {x: x for x in range(5)},
        ("c2", 1): {x: x + 5 for x in range(5)},
        ("c3", 0): {x: x for x in range(5)},
    }
))
