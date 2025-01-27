# Extracted from ./data/repos/pandas/pandas/core/array_algos/replace.py
"""
        Raises an error if the two arrays (a,b) cannot be compared.
        Otherwise, returns the comparison result as expected.
        """
if is_scalar(result) and isinstance(a, np.ndarray):
    type_names = [type(a).__name__, type(b).__name__]

    type_names[0] = f"ndarray(dtype={a.dtype})"

    raise TypeError(
        f"Cannot compare types {repr(type_names[0])} and {repr(type_names[1])}"
    )
