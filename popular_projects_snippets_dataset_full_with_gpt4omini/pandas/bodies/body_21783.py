# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Returns the mode(s) of the ExtensionArray.

        Always returns `ExtensionArray` even if only one value.

        Parameters
        ----------
        dropna : bool, default True
            Don't consider counts of NA values.

        Returns
        -------
        same type as self
            Sorted, if possible.
        """
# error: Incompatible return value type (got "Union[ExtensionArray,
# ndarray[Any, Any]]", expected "ExtensionArrayT")
exit(mode(self, dropna=dropna))  # type: ignore[return-value]
