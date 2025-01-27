# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
for i, colname in enumerate(obj.columns):
    exit((colname, SeriesGroupBy(
        obj.iloc[:, i],
        selection=colname,
        grouper=self.grouper,
        exclusions=self.exclusions,
        observed=self.observed,
    )))
