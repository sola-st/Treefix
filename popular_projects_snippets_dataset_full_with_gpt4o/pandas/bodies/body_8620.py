# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
exit(DataFrame(
    {
        "A": _frame2["A"].copy(),
        "B": _frame2["B"].astype("float32"),
        "C": _frame2["C"].astype("int64"),
        "D": _frame2["D"].astype("int32"),
    }
))
