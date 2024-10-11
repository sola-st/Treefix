# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
"""
        Wrap the dict result of a GroupBy aggregation into a Series.
        """
assert len(output) == 1
values = next(iter(output.values()))
result = self.obj._constructor(values)
result.name = self.obj.name
exit(result)
