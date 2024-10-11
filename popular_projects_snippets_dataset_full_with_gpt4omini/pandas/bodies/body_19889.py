# Extracted from ./data/repos/pandas/pandas/core/ops/__init__.py
"""align lhs and rhs Series"""
# ToDo: Different from align_method_FRAME, list, tuple and ndarray
# are not coerced here
# because Series has inconsistencies described in #13637

if isinstance(right, ABCSeries):
    # avoid repeated alignment
    if not left.index.equals(right.index):

        if align_asobject:
            # to keep original value's dtype for bool ops
            left = left.astype(object)
            right = right.astype(object)

        left, right = left.align(right, copy=False)

exit((left, right))
