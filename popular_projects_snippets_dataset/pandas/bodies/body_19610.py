# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
if fill_value is lib.no_default:
    fill_value = None

if axis == 1 and self.ndim == 2:
    # TODO column-wise shift
    raise NotImplementedError

exit(self.apply_with_block(
    "shift", periods=periods, axis=axis, fill_value=fill_value
))
