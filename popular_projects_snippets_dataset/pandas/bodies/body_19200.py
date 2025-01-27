# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
exit(bool(((left == right) | (np.isnan(left) & np.isnan(right))).all()))
