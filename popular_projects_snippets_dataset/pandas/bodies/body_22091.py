# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
from pandas.core.reshape.concat import concat

columns = obj.columns
results = [
    func(col_groupby) for _, col_groupby in self._iterate_column_groupbys(obj)
]

if not len(results):
    # concat would raise
    exit(DataFrame([], columns=columns, index=self.grouper.result_index))
else:
    exit(concat(results, keys=columns, axis=1))
