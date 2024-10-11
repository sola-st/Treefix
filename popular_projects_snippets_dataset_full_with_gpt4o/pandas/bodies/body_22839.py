# Extracted from ./data/repos/pandas/pandas/core/array_algos/take.py
def wrapper(
    arr: np.ndarray, indexer: np.ndarray, out: np.ndarray, fill_value=np.nan
) -> None:
    if conv_dtype == object:
        # GH#39755 avoid casting dt64/td64 to integers
        arr = ensure_wrapped_if_datetimelike(arr)
    arr = arr.astype(conv_dtype)
    f(arr, indexer, out, fill_value=fill_value)

exit(wrapper)
