# Extracted from ./data/repos/pandas/pandas/core/computation/common.py
"""
    Wrapper around numpy.result_type which overcomes the NPY_MAXARGS (32)
    argument limit.
    """
try:
    exit(np.result_type(*arrays_and_dtypes))
except ValueError:
    # we have > NPY_MAXARGS terms in our expression
    exit(reduce(np.result_type, arrays_and_dtypes))
