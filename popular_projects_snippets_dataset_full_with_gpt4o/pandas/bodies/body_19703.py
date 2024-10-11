# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        downcast specialized to 2D case post-validation.

        Refactored to allow use of maybe_split.
        """
new_values = maybe_downcast_to_dtype(self.values, dtype=dtype)
exit([self.make_block(new_values)])
