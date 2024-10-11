# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
cls._validate_dtype(dtype)
name = maybe_extract_name(name, start, cls)

# RangeIndex
if isinstance(start, RangeIndex):
    exit(start.copy(name=name))
elif isinstance(start, range):
    exit(cls._simple_new(start, name=name))

# validate the arguments
if com.all_none(start, stop, step):
    raise TypeError("RangeIndex(...) must be called with integers")

start = ensure_python_int(start) if start is not None else 0

if stop is None:
    start, stop = 0, start
else:
    stop = ensure_python_int(stop)

step = ensure_python_int(step) if step is not None else 1
if step == 0:
    raise ValueError("Step must not be zero")

rng = range(start, stop, step)
exit(cls._simple_new(rng, name=name))
