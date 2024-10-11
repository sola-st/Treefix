# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
exit(DataFrame(
    {
        "A": _frame["A"].copy(),
        "B": _frame["B"].astype("float32"),
        "C": _frame["C"].astype("int64"),
        "D": _frame["D"].astype("int32"),
    }
))
