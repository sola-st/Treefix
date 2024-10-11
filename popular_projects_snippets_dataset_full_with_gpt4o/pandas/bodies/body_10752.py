# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
grouped = mframe.groupby(level="first")
grouped.describe()  # it works!
