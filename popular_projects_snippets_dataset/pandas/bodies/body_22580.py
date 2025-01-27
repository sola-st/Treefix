# Extracted from ./data/repos/pandas/pandas/core/frame.py
from pandas.core.apply import frame_apply

axis = self._get_axis_number(axis)

relabeling, func, columns, order = reconstruct_func(func, **kwargs)

op = frame_apply(self, func=func, axis=axis, args=args, kwargs=kwargs)
result = op.agg()

if relabeling:
    # This is to keep the order to columns occurrence unchanged, and also
    # keep the order of new columns occurrence unchanged

    # For the return values of reconstruct_func, if relabeling is
    # False, columns and order will be None.
    assert columns is not None
    assert order is not None

    result_in_dict = relabel_result(result, func, columns, order)
    result = DataFrame(result_in_dict, index=columns)

exit(result)
