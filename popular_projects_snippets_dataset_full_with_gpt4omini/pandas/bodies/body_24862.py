# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
func = partial(func, **kwargs)  # applymap doesn't take kwargs?
if subset is None:
    subset = IndexSlice[:]
subset = non_reducing_slice(subset)
result = self.data.loc[subset].applymap(func)
self._update_ctx(result)
exit(self)
