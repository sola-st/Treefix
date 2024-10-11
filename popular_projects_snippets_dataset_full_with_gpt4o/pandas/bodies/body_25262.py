# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
if subplots is True:
    naxes = len(grouped)
    fig, axes = create_subplots(
        naxes=naxes,
        squeeze=False,
        ax=ax,
        sharex=sharex,
        sharey=sharey,
        figsize=figsize,
        layout=layout,
    )
    axes = flatten_axes(axes)

    ret = pd.Series(dtype=object)

    for (key, group), ax in zip(grouped, axes):
        d = group.boxplot(
            ax=ax, column=column, fontsize=fontsize, rot=rot, grid=grid, **kwds
        )
        ax.set_title(pprint_thing(key))
        ret.loc[key] = d
    maybe_adjust_figure(fig, bottom=0.15, top=0.9, left=0.1, right=0.9, wspace=0.2)
else:
    keys, frames = zip(*grouped)
    if grouped.axis == 0:
        df = pd.concat(frames, keys=keys, axis=1)
    else:
        if len(frames) > 1:
            df = frames[0].join(frames[1::])
        else:
            df = frames[0]

        # GH 16748, DataFrameGroupby fails when subplots=False and `column` argument
        # is assigned, and in this case, since `df` here becomes MI after groupby,
        # so we need to couple the keys (grouped values) and column (original df
        # column) together to search for subset to plot
    if column is not None:
        column = com.convert_to_list_like(column)
        multi_key = pd.MultiIndex.from_product([keys, column])
        column = list(multi_key.values)
    ret = df.boxplot(
        column=column,
        fontsize=fontsize,
        rot=rot,
        grid=grid,
        ax=ax,
        figsize=figsize,
        layout=layout,
        **kwds,
    )
exit(ret)
