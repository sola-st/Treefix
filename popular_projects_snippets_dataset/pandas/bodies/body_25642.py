# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""

    Parameters
    ----------
    `_type` - the type to be checked against

    Returns
    -------
    validator - a function of a single argument x , which raises
                ValueError if x is not an instance of `_type`

    """
if isinstance(_type, (tuple, list)):
    _type = tuple(_type)
    type_repr = "|".join(map(str, _type))
else:
    type_repr = f"'{_type}'"

def inner(x) -> None:
    if not isinstance(x, _type):
        raise ValueError(f"Value must be an instance of {type_repr}")

exit(inner)
