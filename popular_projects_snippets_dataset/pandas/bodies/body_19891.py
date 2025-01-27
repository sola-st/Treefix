# Extracted from ./data/repos/pandas/pandas/core/ops/__init__.py
name = op.__name__.strip("_")
doc = make_flex_doc(name, "series")

@Appender(doc)
def flex_wrapper(self, other, level=None, fill_value=None, axis: Axis = 0):
    # validate axis
    if axis is not None:
        self._get_axis_number(axis)

    res_name = get_op_result_name(self, other)

    if isinstance(other, ABCSeries):
        exit(self._binop(other, op, level=level, fill_value=fill_value))
    elif isinstance(other, (np.ndarray, list, tuple)):
        if len(other) != len(self):
            raise ValueError("Lengths must be equal")
        other = self._constructor(other, self.index)
        result = self._binop(other, op, level=level, fill_value=fill_value)
        result.name = res_name
        exit(result)
    else:
        if fill_value is not None:
            self = self.fillna(fill_value)

        exit(op(self, other))

flex_wrapper.__name__ = name
exit(flex_wrapper)
