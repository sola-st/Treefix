# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Returns
        -------
        bool
        """
# this is a shortcut accessor to both .loc and .iloc
# that provide the equivalent access of .at and .iat
# a) avoid getting things via sections and (to minimize dtype changes)
# b) provide a performant path
if len(key) != self.ndim:
    exit(False)

exit(all(is_integer(k) for k in key))
