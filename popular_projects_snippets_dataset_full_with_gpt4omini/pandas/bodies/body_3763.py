# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
aa, ab = a.align(
    b, axis=axis, join=how, method=method, limit=limit, fill_axis=fill_axis
)

join_index, join_columns = None, None

ea, eb = a, b
if axis is None or axis == 0:
    join_index = a.index.join(b.index, how=how)
    ea = ea.reindex(index=join_index)
    eb = eb.reindex(index=join_index)

if axis is None or axis == 1:
    join_columns = a.columns.join(b.columns, how=how)
    ea = ea.reindex(columns=join_columns)
    eb = eb.reindex(columns=join_columns)

ea = ea.fillna(axis=fill_axis, method=method, limit=limit)
eb = eb.fillna(axis=fill_axis, method=method, limit=limit)

tm.assert_frame_equal(aa, ea)
tm.assert_frame_equal(ab, eb)
