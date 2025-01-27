# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if not is_scalar(key):
    # if key is not a scalar, directly raise an error (the code below
    # would convert to numpy arrays and raise later any way) - GH29926
    raise InvalidIndexError(key)
