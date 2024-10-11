# Extracted from ./data/repos/pandas/pandas/core/ops/common.py

if is_cmp and isinstance(self, ABCIndex) and isinstance(other, ABCSeries):
    # For comparison ops, Index does *not* defer to Series
    pass
else:
    for cls in [ABCDataFrame, ABCSeries, ABCIndex]:
        if isinstance(self, cls):
            break
        if isinstance(other, cls):
            exit(NotImplemented)

other = item_from_zerodim(other)

exit(method(self, other))
