# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/misc.py
df = frame._get_numeric_data()
n = df.columns.size
naxes = n * n
fig, axes = create_subplots(naxes=naxes, figsize=figsize, ax=ax, squeeze=False)

# no gaps between subplots
maybe_adjust_figure(fig, wspace=0, hspace=0)

mask = notna(df)

marker = _get_marker_compat(marker)

hist_kwds = hist_kwds or {}
density_kwds = density_kwds or {}

# GH 14855
kwds.setdefault("edgecolors", "none")

boundaries_list = []
for a in df.columns:
    values = df[a].values[mask[a].values]
    rmin_, rmax_ = np.min(values), np.max(values)
    rdelta_ext = (rmax_ - rmin_) * range_padding / 2
    boundaries_list.append((rmin_ - rdelta_ext, rmax_ + rdelta_ext))

for i, a in enumerate(df.columns):
    for j, b in enumerate(df.columns):
        ax = axes[i, j]

        if i == j:
            values = df[a].values[mask[a].values]

            # Deal with the diagonal by drawing a histogram there.
            if diagonal == "hist":
                ax.hist(values, **hist_kwds)

            elif diagonal in ("kde", "density"):
                from scipy.stats import gaussian_kde

                y = values
                gkde = gaussian_kde(y)
                ind = np.linspace(y.min(), y.max(), 1000)
                ax.plot(ind, gkde.evaluate(ind), **density_kwds)

            ax.set_xlim(boundaries_list[i])

        else:
            common = (mask[a] & mask[b]).values

            ax.scatter(
                df[b][common], df[a][common], marker=marker, alpha=alpha, **kwds
            )

            ax.set_xlim(boundaries_list[j])
            ax.set_ylim(boundaries_list[i])

        ax.set_xlabel(b)
        ax.set_ylabel(a)

        if j != 0:
            ax.yaxis.set_visible(False)
        if i != n - 1:
            ax.xaxis.set_visible(False)

if len(df.columns) > 1:
    lim1 = boundaries_list[0]
    locs = axes[0][1].yaxis.get_majorticklocs()
    locs = locs[(lim1[0] <= locs) & (locs <= lim1[1])]
    adj = (locs - lim1[0]) / (lim1[1] - lim1[0])

    lim0 = axes[0][0].get_ylim()
    adj = adj * (lim0[1] - lim0[0]) + lim0[0]
    axes[0][0].yaxis.set_ticks(adj)

    if np.all(locs == locs.astype(int)):
        # if all ticks are int
        locs = locs.astype(int)
    axes[0][0].yaxis.set_ticklabels(locs)

set_ticks_props(axes, xlabelsize=8, xrot=90, ylabelsize=8, yrot=0)

exit(axes)
