# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# Empty series were sometimes causing a segfault (for the functions
# with Cython bounds-checking disabled) or an IndexError.  We just run
# them to ensure they no longer do.  (GH #10228)
empty_series_dti = Series([], index, dtype)
try:
    getattr(empty_series_dti.resample("d", group_keys=False), resample_method)()
except DataError:
    # Ignore these since some combinations are invalid
    # (ex: doing mean with dtype of np.object_)
    pass
