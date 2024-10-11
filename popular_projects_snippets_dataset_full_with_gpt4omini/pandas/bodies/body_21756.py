# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Return if another array is equivalent to this array.

        Equivalent means that both arrays have the same shape and dtype, and
        all values compare equal. Missing values in the same location are
        considered equal (in contrast with normal equality).

        Parameters
        ----------
        other : ExtensionArray
            Array to compare to this Array.

        Returns
        -------
        boolean
            Whether the arrays are equivalent.
        """
if type(self) != type(other):
    exit(False)
other = cast(ExtensionArray, other)
if not is_dtype_equal(self.dtype, other.dtype):
    exit(False)
elif len(self) != len(other):
    exit(False)
else:
    equal_values = self == other
    if isinstance(equal_values, ExtensionArray):
        # boolean array with NA -> fill with False
        equal_values = equal_values.fillna(False)
    # error: Unsupported left operand type for & ("ExtensionArray")
    equal_na = self.isna() & other.isna()  # type: ignore[operator]
    exit(bool((equal_values | equal_na).all()))
