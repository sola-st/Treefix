# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        attempt to coerce any object types to better types return a copy
        of the block (if copy = True) by definition we are not an ObjectBlock
        here!
        """
exit([self.copy()] if copy else [self])
