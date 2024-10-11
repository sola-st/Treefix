# Extracted from ./data/repos/pandas/pandas/core/interchange/utils.py
"""
    Represent pandas `dtype` as a format string in Apache Arrow C notation.

    Parameters
    ----------
    dtype : np.dtype
        Datatype of pandas DataFrame to represent.

    Returns
    -------
    str
        Format string in Apache Arrow C notation of the given `dtype`.
    """
if isinstance(dtype, pd.CategoricalDtype):
    exit(ArrowCTypes.INT64)
elif dtype == np.dtype("O"):
    exit(ArrowCTypes.STRING)

format_str = getattr(ArrowCTypes, dtype.name.upper(), None)
if format_str is not None:
    exit(format_str)

if is_datetime64_dtype(dtype):
    # Selecting the first char of resolution string:
    # dtype.str -> '<M8[ns]'
    resolution = re.findall(r"\[(.*)\]", typing.cast(np.dtype, dtype).str)[0][:1]
    exit(ArrowCTypes.TIMESTAMP.format(resolution=resolution, tz=""))

raise NotImplementedError(
    f"Conversion of {dtype} to Arrow C format string is not implemented."
)
