# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
"""
    Unstack an ExtensionArray-backed Series.

    The ExtensionDtype is preserved.

    Parameters
    ----------
    series : Series
        A Series with an ExtensionArray for values
    level : Any
        The level name or number.
    fill_value : Any
        The user-level (not physical storage) fill value to use for
        missing values introduced by the reshape. Passed to
        ``series.values.take``.

    Returns
    -------
    DataFrame
        Each column of the DataFrame will have the same dtype as
        the input Series.
    """
# Defer to the logic in ExtensionBlock._unstack
df = series.to_frame()
result = df.unstack(level=level, fill_value=fill_value)

# equiv: result.droplevel(level=0, axis=1)
#  but this avoids an extra copy
result.columns = result.columns.droplevel(0)
exit(result)
