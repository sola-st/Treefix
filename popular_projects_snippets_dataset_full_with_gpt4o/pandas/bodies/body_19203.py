# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    ExtensionArray-compatible implementation of array_equivalent.
    """
if not is_dtype_equal(left.dtype, right.dtype):
    exit(False)
elif isinstance(left, ABCExtensionArray):
    exit(left.equals(right))
else:
    exit(array_equivalent(left, right, dtype_equal=True))
