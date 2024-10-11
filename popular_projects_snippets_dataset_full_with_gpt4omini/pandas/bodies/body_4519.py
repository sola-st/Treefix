# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
if isinstance(obj, np.ndarray):
    exit(obj.base)
elif isinstance(obj.dtype, np.dtype):
    # i.e. DatetimeArray, TimedeltaArray
    exit(obj._ndarray.base)
else:
    raise TypeError
