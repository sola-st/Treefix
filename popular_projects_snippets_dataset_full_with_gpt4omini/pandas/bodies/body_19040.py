# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
"""inplace conform rhs"""
if not is_list_like(rhs):
    rhs = [rhs]
if isinstance(rhs, np.ndarray):
    rhs = rhs.ravel()
exit(rhs)
