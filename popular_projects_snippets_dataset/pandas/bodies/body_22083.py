# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
# iterate through columns, see test_transform_exclude_nuisance
#  gets here with non-unique columns
output = {}
inds = []
for i, (colname, sgb) in enumerate(self._iterate_column_groupbys(obj)):
    output[i] = sgb.transform(wrapper)
    inds.append(i)

if not output:
    raise TypeError("Transform function invalid for data types")

columns = obj.columns.take(inds)

result = self.obj._constructor(output, index=obj.index)
result.columns = columns
exit(result)
