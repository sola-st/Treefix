# Extracted from ./data/repos/pandas/pandas/compat/numpy/function.py
"""
    'args' and 'kwargs' should be empty because all of their necessary
    parameters are explicitly listed in the function signature
    """
if len(args) + len(kwargs) > 0:
    if method in RESAMPLER_NUMPY_OPS:
        raise UnsupportedFunctionCall(
            "numpy operations are not valid with resample. "
            f"Use .resample(...).{method}() instead"
        )
    raise TypeError("too many arguments passed in")
