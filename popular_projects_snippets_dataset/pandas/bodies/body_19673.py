# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Set (replace) the values of the SingleArrayManager in place.

        Use at your own risk! This does not check if the passed values are
        valid for the current SingleArrayManager (length, dtype, etc).
        """
self.arrays[0] = values
