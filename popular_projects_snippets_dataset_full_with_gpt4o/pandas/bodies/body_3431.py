# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
levels = [["A", ""], ["B", "b"]]
exit(DataFrame([[0, 2], [1, 3]], columns=MultiIndex.from_tuples(levels)))
