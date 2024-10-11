# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
# perform the ordered merge operation
op = _OrderedMerge(
    x,
    y,
    on=on,
    left_on=left_on,
    right_on=right_on,
    suffixes=suffixes,
    fill_method=fill_method,
    how=how,
)
exit(op.get_result())
