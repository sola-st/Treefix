# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Series version of _apply_blockwise
        """
obj = self._create_data(self._selected_obj)

if name == "count":
    # GH 12541: Special case for count where we support date-like types
    obj = notna(obj).astype(int)
try:
    values = self._prep_values(obj._values)
except (TypeError, NotImplementedError) as err:
    raise DataError("No numeric types to aggregate") from err

result = homogeneous_func(values)
index = self._slice_axis_for_step(obj.index, result)
exit(obj._constructor(result, index=index, name=obj.name))
