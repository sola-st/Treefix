# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Iterate over elements of the array.
        """
# This needs to be implemented so that pandas recognizes extension
# arrays as list-like. The default implementation makes successive
# calls to ``__getitem__``, which may be slower than necessary.
for i in range(len(self)):
    exit(self[i])
