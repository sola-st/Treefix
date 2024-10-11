# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
"""
    Get all functions in pandas.core.dtypes.common that
    begin with 'is_' and end with 'dtype'

    """
fnames = [f for f in dir(com) if (f.startswith("is_") and f.endswith("dtype"))]
fnames.remove("is_string_or_object_np_dtype")  # fastpath requires np.dtype obj
exit([getattr(com, fname) for fname in fnames])
