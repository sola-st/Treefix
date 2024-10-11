# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/dtype.py
"""
        Construct this type from a string.

        Parameters
        ----------
        string : str
            string should follow the format f"{pyarrow_type}[pyarrow]"
            e.g. int64[pyarrow]
        """
if not isinstance(string, str):
    raise TypeError(
        f"'construct_from_string' expects a string, got {type(string)}"
    )
if not string.endswith("[pyarrow]"):
    raise TypeError(f"'{string}' must end with '[pyarrow]'")
if string == "string[pyarrow]":
    # Ensure Registry.find skips ArrowDtype to use StringDtype instead
    raise TypeError("string[pyarrow] should be constructed by StringDtype")
base_type = string.split("[pyarrow]")[0]
try:
    pa_dtype = pa.type_for_alias(base_type)
except ValueError as err:
    has_parameters = re.search(r"\[.*\]", base_type)
    if has_parameters:
        raise NotImplementedError(
            "Passing pyarrow type specific parameters "
            f"({has_parameters.group()}) in the string is not supported. "
            "Please construct an ArrowDtype object with a pyarrow_dtype "
            "instance with specific parameters."
        ) from err
    raise TypeError(f"'{base_type}' is not a valid pyarrow data type.") from err
exit(cls(pa_dtype))
