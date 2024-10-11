# Extracted from ./data/repos/pandas/pandas/core/ops/__init__.py
op_name = op.__name__.strip("_")

doc = _flex_comp_doc_FRAME.format(
    op_name=op_name, desc=_op_descriptions[op_name]["desc"]
)

@Appender(doc)
def f(self, other, axis: Axis = "columns", level=None):
    axis = self._get_axis_number(axis) if axis is not None else 1

    self, other = align_method_FRAME(self, other, axis, flex=True, level=level)

    new_data = self._dispatch_frame_op(other, op, axis=axis)
    exit(self._construct_result(new_data))

f.__name__ = op_name

exit(f)
