# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
axis = self.data._get_axis_number(axis)
obj = self.index if axis == 0 else self.columns

levels_ = refactor_levels(level, obj)
data = DataFrame(obj.to_list()).loc[:, levels_]

if method == "apply":
    result = data.apply(func, axis=0, **kwargs)
elif method == "applymap":
    result = data.applymap(func, **kwargs)

self._update_ctx_header(result, axis)
exit(self)
