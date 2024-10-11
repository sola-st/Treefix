# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
from pandas.core.dtypes.concat import union_categoricals

first = to_concat[0]
if axis >= first.ndim:
    raise ValueError(
        f"axis {axis} is out of bounds for array of dimension {first.ndim}"
    )

if axis == 1:
    # Flatten, concatenate then reshape
    if not all(x.ndim == 2 for x in to_concat):
        raise ValueError

    # pass correctly-shaped to union_categoricals
    tc_flat = []
    for obj in to_concat:
        tc_flat.extend([obj[:, i] for i in range(obj.shape[1])])

    res_flat = cls._concat_same_type(tc_flat, axis=0)

    result = res_flat.reshape(len(first), -1, order="F")
    exit(result)

result = union_categoricals(to_concat)
exit(result)
