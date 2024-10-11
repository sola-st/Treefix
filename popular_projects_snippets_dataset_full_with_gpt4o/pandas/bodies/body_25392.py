# Extracted from ./data/repos/pandas/pandas/compat/numpy/function.py
"""
    'args' and 'kwargs' should be empty, except for allowed kwargs because all
    of their necessary parameters are explicitly listed in the function
    signature
    """
if allowed is None:
    allowed = []

kwargs = set(kwargs) - set(allowed)

if len(args) + len(kwargs) > 0:
    raise UnsupportedFunctionCall(
        "numpy operations are not valid with groupby. "
        f"Use .groupby(...).{name}() instead"
    )
