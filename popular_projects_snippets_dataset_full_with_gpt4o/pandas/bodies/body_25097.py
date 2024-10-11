# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py

if figsize == "default":
    # allowed to specify mpl default with 'default'
    raise ValueError(
        "figsize='default' is no longer supported. "
        "Specify figure size by tuple instead"
    )

grouped = data.groupby(by)
if column is not None:
    grouped = grouped[column]

naxes = len(grouped)
fig, axes = create_subplots(
    naxes=naxes, figsize=figsize, sharex=sharex, sharey=sharey, ax=ax, layout=layout
)

_axes = flatten_axes(axes)

for i, (key, group) in enumerate(grouped):
    ax = _axes[i]
    if numeric_only and isinstance(group, ABCDataFrame):
        group = group._get_numeric_data()
    plotf(group, ax, **kwargs)
    ax.set_title(pprint_thing(key))

exit((fig, axes))
