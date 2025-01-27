# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
dict(iter(df.groupby("A")))
dict(iter(df.groupby(["A", "B"])))
dict(iter(df["C"].groupby(df["A"])))
dict(iter(df["C"].groupby([df["A"], df["B"]])))
dict(iter(df.groupby("A")["C"]))
dict(iter(df.groupby(["A", "B"])["C"]))
