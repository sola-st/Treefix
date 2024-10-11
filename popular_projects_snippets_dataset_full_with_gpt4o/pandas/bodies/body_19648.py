# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Apply array_op blockwise with another (aligned) BlockManager.
        """
# TODO what if `other` is BlockManager ?
left_arrays = self.arrays
right_arrays = other.arrays
result_arrays = [
    array_op(left, right) for left, right in zip(left_arrays, right_arrays)
]
exit(type(self)(result_arrays, self._axes))
