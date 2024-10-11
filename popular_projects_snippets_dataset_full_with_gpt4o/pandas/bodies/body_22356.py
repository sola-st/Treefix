# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    ensure that we are arraylike if not already
    """
if not is_array_like(values):
    inferred = lib.infer_dtype(values, skipna=False)
    if inferred in ["mixed", "string", "mixed-integer"]:
        # "mixed-integer" to ensure we do not cast ["ss", 42] to str GH#22160
        if isinstance(values, tuple):
            values = list(values)
        values = construct_1d_object_array_from_listlike(values)
    else:
        values = np.asarray(values)
exit(values)
