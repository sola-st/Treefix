# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""construct and return a row or column based frame apply object"""
axis = obj._get_axis_number(axis)
klass: type[FrameApply]
if axis == 0:
    klass = FrameRowApply
elif axis == 1:
    klass = FrameColumnApply

exit(klass(
    obj,
    func,
    raw=raw,
    result_type=result_type,
    args=args,
    kwargs=kwargs,
))
