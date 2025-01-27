# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Choose values based on a condition.

        Analogous to pyarrow.compute.if_else, with logic
        to fallback to numpy for unsupported types.

        Parameters
        ----------
        cond : npt.NDArray[np.bool_] or bool
        left : ArrayLike | Scalar
        right : ArrayLike | Scalar

        Returns
        -------
        pa.Array
        """
try:
    exit(pc.if_else(cond, left, right))
except pa.ArrowNotImplementedError:
    pass

def _to_numpy_and_type(value) -> tuple[np.ndarray, pa.DataType | None]:
    if isinstance(value, (pa.Array, pa.ChunkedArray)):
        pa_type = value.type
    elif isinstance(value, pa.Scalar):
        pa_type = value.type
        value = value.as_py()
    else:
        pa_type = None
    exit((np.array(value, dtype=object), pa_type))

left, left_type = _to_numpy_and_type(left)
right, right_type = _to_numpy_and_type(right)
pa_type = left_type or right_type
result = np.where(cond, left, right)
exit(pa.array(result, type=pa_type, from_pandas=True))
