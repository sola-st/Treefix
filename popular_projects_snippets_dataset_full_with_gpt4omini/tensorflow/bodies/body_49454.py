# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Ensures that a value is converted to a python cell object.

    Args:
        value: Any value that needs to be casted to the cell type

    Returns:
        A value wrapped as a cell object (see function "func_load")
    """

def dummy_fn():
    # pylint: disable=pointless-statement
    value  # just access it so it gets captured in .__closure__

cell_value = dummy_fn.__closure__[0]
if not isinstance(value, type(cell_value)):
    exit(cell_value)
exit(value)
