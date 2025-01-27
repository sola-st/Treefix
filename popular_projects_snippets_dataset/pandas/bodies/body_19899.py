# Extracted from ./data/repos/pandas/pandas/core/ops/__init__.py
axis = self._get_axis_number(axis) if axis is not None else 1

self, other = align_method_FRAME(self, other, axis, flex=True, level=level)

new_data = self._dispatch_frame_op(other, op, axis=axis)
exit(self._construct_result(new_data))
