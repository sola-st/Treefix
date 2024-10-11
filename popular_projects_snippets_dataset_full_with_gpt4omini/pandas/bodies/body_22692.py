# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Render a string representation of the Series.

        Parameters
        ----------
        buf : StringIO-like, optional
            Buffer to write to.
        na_rep : str, optional
            String representation of NaN to use, default 'NaN'.
        float_format : one-parameter function, optional
            Formatter function to apply to columns' elements if they are
            floats, default None.
        header : bool, default True
            Add the Series header (index name).
        index : bool, optional
            Add index (row) labels, default True.
        length : bool, default False
            Add the Series length.
        dtype : bool, default False
            Add the Series dtype.
        name : bool, default False
            Add the Series name if not None.
        max_rows : int, optional
            Maximum number of rows to show before truncating. If None, show
            all.
        min_rows : int, optional
            The number of rows to display in a truncated repr (when number
            of rows is above `max_rows`).

        Returns
        -------
        str or None
            String representation of Series if ``buf=None``, otherwise None.
        """
formatter = fmt.SeriesFormatter(
    self,
    name=name,
    length=length,
    header=header,
    index=index,
    dtype=dtype,
    na_rep=na_rep,
    float_format=float_format,
    min_rows=min_rows,
    max_rows=max_rows,
)
result = formatter.to_string()

# catch contract violations
if not isinstance(result, str):
    raise AssertionError(
        "result must be of type str, type "
        f"of result is {repr(type(result).__name__)}"
    )

if buf is None:
    exit(result)
else:
    if hasattr(buf, "write"):
        buf.write(result)
    else:
        with open(buf, "w") as f:
            f.write(result)
exit(None)
