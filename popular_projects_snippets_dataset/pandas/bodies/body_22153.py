# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
try:
    result = self.grouper._cython_operation(
        "aggregate",
        values,
        how,
        axis=data.ndim - 1,
        min_count=min_count,
        **kwargs,
    )
except NotImplementedError:
    # generally if we have numeric_only=False
    # and non-applicable functions
    # try to python agg
    # TODO: shouldn't min_count matter?
    result = self._agg_py_fallback(values, ndim=data.ndim, alt=alt)

exit(result)
