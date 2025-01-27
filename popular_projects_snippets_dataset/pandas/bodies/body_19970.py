# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Require integer args. (and convert to label arguments)
        """
for i in key:
    if not is_integer(i):
        raise ValueError("iAt based indexing can only have integer indexers")
exit(key)
