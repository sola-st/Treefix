# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
            Wrap user supplied function to work around numpy issue.

            see https://github.com/numpy/numpy/issues/8352
            """

def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    if isinstance(result, str):
        result = np.array(result, dtype=object)
    exit(result)

exit(wrapper)
