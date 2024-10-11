# Extracted from ./data/repos/pandas/pandas/core/nanops.py
# #18044 reference this behavior to fix rolling skew/kurt issue
if isinstance(arg, np.ndarray):
    with np.errstate(invalid="ignore"):
        exit(np.where(np.abs(arg) < 1e-14, 0, arg))
else:
    exit(arg.dtype.type(0) if np.abs(arg) < 1e-14 else arg)
