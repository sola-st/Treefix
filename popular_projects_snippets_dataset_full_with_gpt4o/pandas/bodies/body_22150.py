# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
func = com.is_builtin_func(func)
f = lambda x: func(x, *args, **kwargs)

# iterate through "columns" ex exclusions to populate output dict
output: dict[base.OutputKey, ArrayLike] = {}

if self.ngroups == 0:
    # agg_series below assumes ngroups > 0
    exit(self._python_apply_general(f, self._selected_obj, is_agg=True))

for idx, obj in enumerate(self._iterate_slices()):
    name = obj.name
    result = self.grouper.agg_series(obj, f)
    key = base.OutputKey(label=name, position=idx)
    output[key] = result

if not output:
    exit(self._python_apply_general(f, self._selected_obj))

exit(self._wrap_aggregated_output(output))
