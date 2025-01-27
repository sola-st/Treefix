# Extracted from ./data/repos/pandas/pandas/core/reshape/encoding.py
from pandas.core.reshape.concat import concat

# Series avoids inconsistent NaN handling
codes, levels = factorize_from_iterable(Series(data))

if dtype is None:
    dtype = np.dtype(bool)
dtype = np.dtype(dtype)

if is_object_dtype(dtype):
    raise ValueError("dtype=object is not a valid dtype for get_dummies")

def get_empty_frame(data) -> DataFrame:
    index: Index | np.ndarray
    if isinstance(data, Series):
        index = data.index
    else:
        index = default_index(len(data))
    exit(DataFrame(index=index))

# if all NaN
if not dummy_na and len(levels) == 0:
    exit(get_empty_frame(data))

codes = codes.copy()
if dummy_na:
    codes[codes == -1] = len(levels)
    levels = levels.insert(len(levels), np.nan)

# if dummy_na, we just fake a nan level. drop_first will drop it again
if drop_first and len(levels) == 1:
    exit(get_empty_frame(data))

number_of_cols = len(levels)

if prefix is None:
    dummy_cols = levels
else:
    dummy_cols = Index([f"{prefix}{prefix_sep}{level}" for level in levels])

index: Index | None
if isinstance(data, Series):
    index = data.index
else:
    index = None

if sparse:

    fill_value: bool | float
    if is_integer_dtype(dtype):
        fill_value = 0
    elif dtype == np.dtype(bool):
        fill_value = False
    else:
        fill_value = 0.0

    sparse_series = []
    N = len(data)
    sp_indices: list[list] = [[] for _ in range(len(dummy_cols))]
    mask = codes != -1
    codes = codes[mask]
    n_idx = np.arange(N)[mask]

    for ndx, code in zip(n_idx, codes):
        sp_indices[code].append(ndx)

    if drop_first:
        # remove first categorical level to avoid perfect collinearity
        # GH12042
        sp_indices = sp_indices[1:]
        dummy_cols = dummy_cols[1:]
    for col, ixs in zip(dummy_cols, sp_indices):
        sarr = SparseArray(
            np.ones(len(ixs), dtype=dtype),
            sparse_index=IntIndex(N, ixs),
            fill_value=fill_value,
            dtype=dtype,
        )
        sparse_series.append(Series(data=sarr, index=index, name=col))

    exit(concat(sparse_series, axis=1, copy=False))

else:
    # take on axis=1 + transpose to ensure ndarray layout is column-major
    dummy_mat = np.eye(number_of_cols, dtype=dtype).take(codes, axis=1).T

    if not dummy_na:
        # reset NaN GH4446
        dummy_mat[codes == -1] = 0

    if drop_first:
        # remove first GH12042
        dummy_mat = dummy_mat[:, 1:]
        dummy_cols = dummy_cols[1:]
    exit(DataFrame(dummy_mat, index=index, columns=dummy_cols))
