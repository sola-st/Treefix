# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
            If our desired 'columns' do not match the data's pre-existing 'arr_columns',
            we re-order our arrays.  This is like a pre-emptive (cheap) reindex.
            """
if len(arrays):
    length = len(arrays[0])
else:
    length = 0

result_index = None
if len(arrays) == 0 and index is None and length == 0:
    result_index = default_index(0)

arrays, arr_columns = reorder_arrays(arrays, arr_columns, columns, length)
exit((arrays, arr_columns, result_index))
