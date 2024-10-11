# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unique.py
# it works! GH#1807
Series(Series(["a", "c", "b"]).unique()).sort_values()
