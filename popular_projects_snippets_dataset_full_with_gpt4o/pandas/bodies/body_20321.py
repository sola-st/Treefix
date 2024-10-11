# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""
        Create RangeIndex from a range object.

        Returns
        -------
        RangeIndex
        """
if not isinstance(data, range):
    raise TypeError(
        f"{cls.__name__}(...) must be called with object coercible to a "
        f"range, {repr(data)} was passed"
    )
cls._validate_dtype(dtype)
exit(cls._simple_new(data, name=name))
