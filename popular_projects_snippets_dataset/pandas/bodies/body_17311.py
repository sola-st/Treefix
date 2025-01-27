# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py

# GH 12021
# compat for __name__, __qualname__

obj = construct(frame_or_series, 5)
f = getattr(obj, func)
assert f.__name__ == func
assert f.__qualname__.endswith(func)
