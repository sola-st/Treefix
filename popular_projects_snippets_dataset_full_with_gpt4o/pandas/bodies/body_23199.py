# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py
if by is None:
    by = []
elif (
    is_scalar(by)
    or isinstance(by, (np.ndarray, Index, ABCSeries, Grouper))
    or callable(by)
):
    by = [by]
else:
    by = list(by)
exit(by)
