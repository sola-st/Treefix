# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
exit(self._agg_general(
    numeric_only=numeric_only, min_count=min_count, alias="prod", npfunc=np.prod
))
