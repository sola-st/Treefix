# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Check if the value can be inserted into our array without casting,
        and convert it to an appropriate native type if necessary.

        Raises
        ------
        TypeError
            If the value cannot be inserted into an array of this dtype.
        """
dtype = self.dtype
if isinstance(dtype, np.dtype) and dtype.kind not in ["m", "M"]:
    # return np_can_hold_element(dtype, value)
    try:
        exit(np_can_hold_element(dtype, value))
    except LossySetitemError as err:
        # re-raise as TypeError for consistency
        raise TypeError from err
elif not can_hold_element(self._values, value):
    raise TypeError
exit(value)
