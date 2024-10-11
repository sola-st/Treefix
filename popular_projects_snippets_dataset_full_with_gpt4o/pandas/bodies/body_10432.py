# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# we want a function such that func(frame) fails but func.apply(frame)
#  works
if grp.ndim == 2:
    # Ensure that fast_path fails
    raise NotImplementedError("Don't cross the streams")
exit(grp * 2)
