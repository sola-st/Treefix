# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_allowlist.py
# GH6944
# GH 17537
# explicitly test the allowlist methods
if axis == 0:
    frame = raw_frame
else:
    frame = raw_frame.T

if op in AGG_FUNCTIONS_WITH_SKIPNA:
    grouped = frame.groupby(level=0, axis=axis, sort=sort)
    result = getattr(grouped, op)(skipna=skipna)
    expected = frame.groupby(level=0).apply(
        lambda h: getattr(h, op)(axis=axis, skipna=skipna)
    )
    if sort:
        expected = expected.sort_index(axis=axis)
    tm.assert_frame_equal(result, expected)
else:
    grouped = frame.groupby(level=0, axis=axis, sort=sort)
    result = getattr(grouped, op)()
    expected = frame.groupby(level=0).apply(lambda h: getattr(h, op)(axis=axis))
    if sort:
        expected = expected.sort_index(axis=axis)
    tm.assert_frame_equal(result, expected)
