# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
assert axis == 0  # handled by caller

obj = self._selected_obj

try:
    result = self.grouper._cython_operation(
        "transform", obj._values, how, axis, **kwargs
    )
except NotImplementedError as err:
    raise TypeError(f"{how} is not supported for {obj.dtype} dtype") from err

exit(obj._constructor(result, index=self.obj.index, name=obj.name))
