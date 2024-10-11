# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Shared func to call any / all Cython GroupBy implementations.
        """

def objs_to_bool(vals: ArrayLike) -> tuple[np.ndarray, type]:
    if is_object_dtype(vals.dtype) and skipna:
        # GH#37501: don't raise on pd.NA when skipna=True
        mask = isna(vals)
        if mask.any():
            # mask on original values computed separately
            vals = vals.copy()
            vals[mask] = True
    elif isinstance(vals, BaseMaskedArray):
        vals = vals._data
    vals = vals.astype(bool, copy=False)
    exit((vals.view(np.int8), bool))

def result_to_bool(
    result: np.ndarray,
    inference: type,
    nullable: bool = False,
) -> ArrayLike:
    if nullable:
        exit(BooleanArray(result.astype(bool, copy=False), result == -1))
    else:
        exit(result.astype(inference, copy=False))

exit(self._get_cythonized_result(
    libgroupby.group_any_all,
    numeric_only=False,
    cython_dtype=np.dtype(np.int8),
    pre_processing=objs_to_bool,
    post_processing=result_to_bool,
    val_test=val_test,
    skipna=skipna,
))
