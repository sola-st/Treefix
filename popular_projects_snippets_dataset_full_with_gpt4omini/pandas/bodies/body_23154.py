# Extracted from ./data/repos/pandas/pandas/core/apply.py
result = func(*args, **kwargs)
if isinstance(result, str):
    result = np.array(result, dtype=object)
exit(result)
