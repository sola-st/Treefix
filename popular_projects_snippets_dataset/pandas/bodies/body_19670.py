# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Set values with indexer.

        For SingleArrayManager, this backs s[indexer] = value

        See `setitem_inplace` for a version that works inplace and doesn't
        return a new Manager.
        """
if isinstance(indexer, np.ndarray) and indexer.ndim > self.ndim:
    raise ValueError(f"Cannot set values with ndim > {self.ndim}")
exit(self.apply_with_block("setitem", indexer=indexer, value=value))
