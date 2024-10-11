# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""
        Return the number of bytes in the underlying data.
        """
rng = self._range
exit(getsizeof(rng) + sum(
    getsizeof(getattr(rng, attr_name))
    for attr_name in ["start", "stop", "step"]
))
