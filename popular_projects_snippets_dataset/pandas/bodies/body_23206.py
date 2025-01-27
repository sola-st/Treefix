# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
op = _MergeOperation(
    left,
    right,
    how=how,
    on=on,
    left_on=left_on,
    right_on=right_on,
    left_index=left_index,
    right_index=right_index,
    sort=sort,
    suffixes=suffixes,
    indicator=indicator,
    validate=validate,
)
exit(op.get_result(copy=copy))
