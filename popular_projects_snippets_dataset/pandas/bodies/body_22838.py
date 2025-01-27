# Extracted from ./data/repos/pandas/pandas/core/array_algos/take.py
if conv_dtype == object:
    # GH#39755 avoid casting dt64/td64 to integers
    arr = ensure_wrapped_if_datetimelike(arr)
arr = arr.astype(conv_dtype)
f(arr, indexer, out, fill_value=fill_value)
