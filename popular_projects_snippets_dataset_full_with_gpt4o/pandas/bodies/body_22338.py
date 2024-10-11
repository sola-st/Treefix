# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
    Return our appropriate resampler when grouping as well.
    """
# .resample uses 'on' similar to how .groupby uses 'key'
tg = TimeGrouper(freq=rule, key=on, **kwargs)
resampler = tg._get_resampler(groupby.obj, kind=kind)
exit(resampler._get_resampler_for_grouping(groupby=groupby, key=tg.key))
