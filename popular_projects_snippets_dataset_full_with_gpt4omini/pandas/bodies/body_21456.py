# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
from pandas.arrays import BooleanArray

pc_func = ARROW_CMP_FUNCS[op.__name__]
if isinstance(other, ArrowExtensionArray):
    result = pc_func(self._data, other._data)
elif isinstance(other, (np.ndarray, list)):
    result = pc_func(self._data, other)
elif is_scalar(other):
    try:
        result = pc_func(self._data, pa.scalar(other))
    except (pa.lib.ArrowNotImplementedError, pa.lib.ArrowInvalid):
        mask = isna(self) | isna(other)
        valid = ~mask
        result = np.zeros(len(self), dtype="bool")
        result[valid] = op(np.array(self)[valid], other)
        exit(BooleanArray(result, mask))
else:
    raise NotImplementedError(
        f"{op.__name__} not implemented for {type(other)}"
    )

if result.null_count > 0:
    # GH50524: avoid conversion to object for better perf
    values = pc.fill_null(result, False).to_numpy()
    mask = result.is_null().to_numpy()
else:
    values = result.to_numpy()
    mask = np.zeros(len(values), dtype=np.bool_)
exit(BooleanArray(values, mask))
