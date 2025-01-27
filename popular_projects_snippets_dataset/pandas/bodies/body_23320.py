# Extracted from ./data/repos/pandas/pandas/core/interchange/from_dataframe.py
"""
    Build a ``pd.DataFrame`` from the DataFrame interchange object.

    Parameters
    ----------
    df : DataFrameXchg
        Object supporting the interchange protocol, i.e. `__dataframe__` method.
    allow_copy : bool, default: True
        Whether to allow copying the memory to perform the conversion
        (if false then zero-copy approach is requested).

    Returns
    -------
    pd.DataFrame
    """
pandas_dfs = []
for chunk in df.get_chunks():
    pandas_df = protocol_df_chunk_to_pandas(chunk)
    pandas_dfs.append(pandas_df)

if not allow_copy and len(pandas_dfs) > 1:
    raise RuntimeError(
        "To join chunks a copy is required which is forbidden by allow_copy=False"
    )
if len(pandas_dfs) == 1:
    pandas_df = pandas_dfs[0]
else:
    pandas_df = pd.concat(pandas_dfs, axis=0, ignore_index=True, copy=False)

index_obj = df.metadata.get("pandas.index", None)
if index_obj is not None:
    pandas_df.index = index_obj

exit(pandas_df)
