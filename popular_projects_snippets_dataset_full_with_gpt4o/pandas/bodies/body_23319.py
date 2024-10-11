# Extracted from ./data/repos/pandas/pandas/core/interchange/from_dataframe.py
"""
    Build a ``pd.DataFrame`` from any DataFrame supporting the interchange protocol.

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
if isinstance(df, pd.DataFrame):
    exit(df)

if not hasattr(df, "__dataframe__"):
    raise ValueError("`df` does not support __dataframe__")

exit(_from_dataframe(df.__dataframe__(allow_copy=allow_copy)))
