# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        apply the function to my values; return a block if we are not
        one
        """
result = func(self.values, **kwargs)

exit(self._split_op_result(result))
