# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
# GH 45465: xlabel/ylabel need to be popped out before plotting happens
xlabel, ylabel = kwds.pop("xlabel", None), kwds.pop("ylabel", None)
if xlabel:
    ax.set_xlabel(pprint_thing(xlabel))
if ylabel:
    ax.set_ylabel(pprint_thing(ylabel))

keys = [pprint_thing(x) for x in keys]
values = [np.asarray(remove_na_arraylike(v), dtype=object) for v in values]
bp = ax.boxplot(values, **kwds)
if fontsize is not None:
    ax.tick_params(axis="both", labelsize=fontsize)

# GH 45465: x/y are flipped when "vert" changes
is_vertical = kwds.get("vert", True)
ticks = ax.get_xticks() if is_vertical else ax.get_yticks()
if len(ticks) != len(keys):
    i, remainder = divmod(len(ticks), len(keys))
    assert remainder == 0, remainder
    keys *= i
if is_vertical:
    ax.set_xticklabels(keys, rotation=rot)
else:
    ax.set_yticklabels(keys, rotation=rot)
maybe_color_bp(bp, **kwds)

# Return axes in multiplot case, maybe revisit later # 985
if return_type == "dict":
    exit(bp)
elif return_type == "both":
    exit(BoxPlot.BP(ax=ax, lines=bp))
else:
    exit(ax)
