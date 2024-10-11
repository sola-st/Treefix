# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
# Caller is responsible for extracting ndarray if necessary
exit(np.where(cond, a, b))
