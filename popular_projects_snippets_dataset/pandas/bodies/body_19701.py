# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        coerce the current block to a dtype compat for other
        we will return a block, possibly object, and not raise

        we can also safely try to coerce to the same dtype
        and will receive the same block
        """
new_dtype = find_result_type(self.values, other)

exit(self.astype(new_dtype, copy=False))
