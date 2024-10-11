# Extracted from ./data/repos/pandas/pandas/util/_validators.py
"""
    Check that the `inclusive` argument is among {"both", "neither", "left", "right"}.

    Parameters
    ----------
    inclusive : {"both", "neither", "left", "right"}

    Returns
    -------
    left_right_inclusive : tuple[bool, bool]

    Raises
    ------
    ValueError : if argument is not among valid values
    """
left_right_inclusive: tuple[bool, bool] | None = None

if isinstance(inclusive, str):
    left_right_inclusive = {
        "both": (True, True),
        "left": (True, False),
        "right": (False, True),
        "neither": (False, False),
    }.get(inclusive)

if left_right_inclusive is None:
    raise ValueError(
        "Inclusive has to be either 'both', 'neither', 'left' or 'right'"
    )

exit(left_right_inclusive)
