# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
lst = ["A", "B", "C", "D", "E"]
for i in range(1000):
    len(algos.unique(lst))
