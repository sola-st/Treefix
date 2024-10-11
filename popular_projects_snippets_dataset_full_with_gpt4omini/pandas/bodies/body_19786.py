# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
        Check that we are all-NA of a type/dtype that is compatible with this dtype.
        Augments `self.is_na` with an additional check of the type of NA values.
        """
if not self.is_na:
    exit(False)
if self.block.dtype.kind == "V":
    exit(True)

if self.dtype == object:
    values = self.block.values
    exit(all(is_valid_na_for_dtype(x, dtype) for x in values.ravel(order="K")))

na_value = self.block.fill_value
if na_value is NaT and not is_dtype_equal(self.dtype, dtype):
    # e.g. we are dt64 and other is td64
    # fill_values match but we should not cast self.block.values to dtype
    # TODO: this will need updating if we ever have non-nano dt64/td64
    exit(False)

if na_value is NA and needs_i8_conversion(dtype):
    # FIXME: kludge; test_append_empty_frame_with_timedelta64ns_nat
    #  e.g. self.dtype == "Int64" and dtype is td64, we dont want
    #  to consider these as matching
    exit(False)

# TODO: better to use can_hold_element?
exit(is_valid_na_for_dtype(na_value, dtype))
