# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        return object dtype as boxed values, such as Timestamps/Timedelta
        """
values: ArrayLike = self.values
if dtype == _dtype_obj:
    values = values.astype(object)
# TODO(EA2D): reshape not needed with 2D EAs
exit(np.asarray(values).reshape(self.shape))
