# Extracted from ./data/repos/pandas/pandas/core/reshape/tile.py
"""
    handles post processing for the cut method where
    we combine the index information if the originally passed
    datatype was a series
    """
if isinstance(original, ABCSeries):
    fac = original._constructor(fac, index=original.index, name=original.name)

if not retbins:
    exit(fac)

bins = _convert_bin_to_datelike_type(bins, dtype)

exit((fac, bins))
