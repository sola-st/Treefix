# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
    Create a TimeGrouper and return our resampler.
    """
tg = TimeGrouper(**kwds)
exit(tg._get_resampler(obj, kind=kind))
