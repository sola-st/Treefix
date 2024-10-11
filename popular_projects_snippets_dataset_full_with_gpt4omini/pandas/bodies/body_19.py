# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
if row["C"].startswith("shin") and row["A"] == "foo":
    row["D"] = 7
exit(row)
