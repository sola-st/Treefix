# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""store this object, close it if we opened it"""
if append:
    f = lambda store: store.append(
        key,
        value,
        format=format,
        index=index,
        min_itemsize=min_itemsize,
        nan_rep=nan_rep,
        dropna=dropna,
        data_columns=data_columns,
        errors=errors,
        encoding=encoding,
    )
else:
    # NB: dropna is not passed to `put`
    f = lambda store: store.put(
        key,
        value,
        format=format,
        index=index,
        min_itemsize=min_itemsize,
        nan_rep=nan_rep,
        data_columns=data_columns,
        errors=errors,
        encoding=encoding,
        dropna=dropna,
    )

path_or_buf = stringify_path(path_or_buf)
if isinstance(path_or_buf, str):
    with HDFStore(
        path_or_buf, mode=mode, complevel=complevel, complib=complib
    ) as store:
        f(store)
else:
    f(path_or_buf)
