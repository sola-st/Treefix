# Extracted from ./data/repos/pandas/pandas/io/pytables.py

# validate the version
self.validate_version(where)

# infer the data kind
if not self.infer_axes():
    exit(None)

result = self._read_axes(where=where, start=start, stop=stop)

info = (
    self.info.get(self.non_index_axes[0][0], {})
    if len(self.non_index_axes)
    else {}
)

inds = [i for i, ax in enumerate(self.axes) if ax is self.index_axes[0]]
assert len(inds) == 1
ind = inds[0]

index = result[ind][0]

frames = []
for i, a in enumerate(self.axes):
    if a not in self.values_axes:
        continue
    index_vals, cvalues = result[i]

    # we could have a multi-index constructor here
    # ensure_index doesn't recognized our list-of-tuples here
    if info.get("type") != "MultiIndex":
        cols = Index(index_vals)
    else:
        cols = MultiIndex.from_tuples(index_vals)

    names = info.get("names")
    if names is not None:
        cols.set_names(names, inplace=True)

    if self.is_transposed:
        values = cvalues
        index_ = cols
        cols_ = Index(index, name=getattr(index, "name", None))
    else:
        values = cvalues.T
        index_ = Index(index, name=getattr(index, "name", None))
        cols_ = cols

    # if we have a DataIndexableCol, its shape will only be 1 dim
    if values.ndim == 1 and isinstance(values, np.ndarray):
        values = values.reshape((1, values.shape[0]))

    if isinstance(values, np.ndarray):
        df = DataFrame(values.T, columns=cols_, index=index_)
    elif isinstance(values, Index):
        df = DataFrame(values, columns=cols_, index=index_)
    else:
        # Categorical
        df = DataFrame._from_arrays([values], columns=cols_, index=index_)
    assert (df.dtypes == values.dtype).all(), (df.dtypes, values.dtype)
    frames.append(df)

if len(frames) == 1:
    df = frames[0]
else:
    df = concat(frames, axis=1)

selection = Selection(self, where=where, start=start, stop=stop)
# apply the selection filters & axis orderings
df = self.process_axes(df, selection=selection, columns=columns)

exit(df)
