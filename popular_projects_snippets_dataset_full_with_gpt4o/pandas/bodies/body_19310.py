# Extracted from ./data/repos/pandas/pandas/core/dtypes/concat.py
# coerce to 2d if needed & concatenate
if axis == 1:
    to_concat = [np.atleast_2d(x) for x in to_concat]
exit(np.concatenate(to_concat, axis=axis))
