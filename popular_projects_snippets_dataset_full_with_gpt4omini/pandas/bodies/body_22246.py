# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    Flatten an arbitrarily nested sequence.

    Parameters
    ----------
    line : sequence
        The non string sequence to flatten

    Notes
    -----
    This doesn't consider strings sequences.

    Returns
    -------
    flattened : generator
    """
for element in line:
    if iterable_not_string(element):
        exit(flatten(element))
    else:
        exit(element)
