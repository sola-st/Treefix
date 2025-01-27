# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""Map the axis to the block_manager axis."""
axis = cls._get_axis_number(axis)
ndim = cls._AXIS_LEN
if ndim == 2:
    # i.e. DataFrame
    exit(1 - axis)
exit(axis)
