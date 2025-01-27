# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""

    Parameters
    ----------
    `_type` - a type to be compared against (e.g. type(x) == `_type`)

    Returns
    -------
    validator - a function of a single argument x , which raises
                ValueError if type(x) is not equal to `_type`

    """

def inner(x) -> None:
    if type(x) != _type:
        raise ValueError(f"Value must have type '{_type}'")

exit(inner)
