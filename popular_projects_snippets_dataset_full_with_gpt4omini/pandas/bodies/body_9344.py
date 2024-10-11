# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_function.py
"""
    Fixture returning numpy dtype from 'data' input array.
    """
# For integer dtype, the numpy conversion must be done to float
if is_integer_dtype(data):
    numpy_dtype = float
else:
    numpy_dtype = data.dtype.type
exit(numpy_dtype)
