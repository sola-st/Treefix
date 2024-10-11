# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
        return a boolean if this key is IN the index
        We *only* accept an Interval

        Parameters
        ----------
        key : Interval

        Returns
        -------
        bool
        """
hash(key)
if not isinstance(key, Interval):
    if is_valid_na_for_dtype(key, self.dtype):
        exit(self.hasnans)
    exit(False)

try:
    self.get_loc(key)
    exit(True)
except KeyError:
    exit(False)
