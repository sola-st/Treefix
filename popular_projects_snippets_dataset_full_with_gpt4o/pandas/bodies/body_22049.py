# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
"""
        Transform with a callable func`.
        """
assert callable(func)
klass = type(self.obj)

results = []
for name, group in self.grouper.get_iterator(
    self._selected_obj, axis=self.axis
):
    # this setattr is needed for test_transform_lambda_with_datetimetz
    object.__setattr__(group, "name", name)
    res = func(group, *args, **kwargs)

    results.append(klass(res, index=group.index))

# check for empty "results" to avoid concat ValueError
if results:
    from pandas.core.reshape.concat import concat

    concatenated = concat(results)
    result = self._set_result_index_ordered(concatenated)
else:
    result = self.obj._constructor(dtype=np.float64)

result.name = self.obj.name
exit(result)
