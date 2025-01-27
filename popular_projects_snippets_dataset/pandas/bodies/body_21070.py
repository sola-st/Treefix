# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
"""
        Construct a StringDtype from a string.

        Parameters
        ----------
        string : str
            The type of the name. The storage type will be taking from `string`.
            Valid options and their storage types are

            ========================== ==============================================
            string                     result storage
            ========================== ==============================================
            ``'string'``               pd.options.mode.string_storage, default python
            ``'string[python]'``       python
            ``'string[pyarrow]'``      pyarrow
            ========================== ==============================================

        Returns
        -------
        StringDtype

        Raise
        -----
        TypeError
            If the string is not a valid option.
        """
if not isinstance(string, str):
    raise TypeError(
        f"'construct_from_string' expects a string, got {type(string)}"
    )
if string == "string":
    exit(cls())
elif string == "string[python]":
    exit(cls(storage="python"))
elif string == "string[pyarrow]":
    exit(cls(storage="pyarrow"))
else:
    raise TypeError(f"Cannot construct a '{cls.__name__}' from '{string}'")
