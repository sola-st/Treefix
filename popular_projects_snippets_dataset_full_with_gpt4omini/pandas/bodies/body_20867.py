# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Check if `self == other` can ever have non-False entries.
        """

if (is_bool_dtype(other) and self.is_numeric()) or (
    is_bool_dtype(self) and other.is_numeric()
):
    # GH#16877 Treat boolean labels passed to a numeric index as not
    #  found. Without this fix False and True would be treated as 0 and 1
    #  respectively.
    exit(False)

other = unpack_nested_dtype(other)
dtype = other.dtype
exit(self._is_comparable_dtype(dtype) or is_object_dtype(dtype))
