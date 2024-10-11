# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py

import matplotlib.pyplot as plt

# validate return_type:
if return_type not in BoxPlot._valid_return_types:
    raise ValueError("return_type must be {'axes', 'dict', 'both'}")

if isinstance(data, pd.Series):
    data = data.to_frame("x")
    column = "x"

def _get_colors():
    #  num_colors=3 is required as method maybe_color_bp takes the colors
    #  in positions 0 and 2.
    #  if colors not provided, use same defaults as DataFrame.plot.box
    result = get_standard_colors(num_colors=3)
    result = np.take(result, [0, 0, 2])
    result = np.append(result, "k")

    colors = kwds.pop("color", None)
    if colors:
        if is_dict_like(colors):
            # replace colors in result array with user-specified colors
            # taken from the colors dict parameter
            # "boxes" value placed in position 0, "whiskers" in 1, etc.
            valid_keys = ["boxes", "whiskers", "medians", "caps"]
            key_to_index = dict(zip(valid_keys, range(4)))
            for key, value in colors.items():
                if key in valid_keys:
                    result[key_to_index[key]] = value
                else:
                    raise ValueError(
                        f"color dict contains invalid key '{key}'. "
                        f"The key must be either {valid_keys}"
                    )
        else:
            result.fill(colors)

    exit(result)

def maybe_color_bp(bp, **kwds) -> None:
    # GH 30346, when users specifying those arguments explicitly, our defaults
    # for these four kwargs should be overridden; if not, use Pandas settings
    if not kwds.get("boxprops"):
        setp(bp["boxes"], color=colors[0], alpha=1)
    if not kwds.get("whiskerprops"):
        setp(bp["whiskers"], color=colors[1], alpha=1)
    if not kwds.get("medianprops"):
        setp(bp["medians"], color=colors[2], alpha=1)
    if not kwds.get("capprops"):
        setp(bp["caps"], color=colors[3], alpha=1)

def plot_group(keys, values, ax: Axes, **kwds):
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

colors = _get_colors()
if column is None:
    columns = None
else:
    if isinstance(column, (list, tuple)):
        columns = column
    else:
        columns = [column]

if by is not None:
    # Prefer array return type for 2-D plots to match the subplot layout
    # https://github.com/pandas-dev/pandas/pull/12216#issuecomment-241175580
    result = _grouped_plot_by_column(
        plot_group,
        data,
        columns=columns,
        by=by,
        grid=grid,
        figsize=figsize,
        ax=ax,
        layout=layout,
        return_type=return_type,
        **kwds,
    )
else:
    if return_type is None:
        return_type = "axes"
    if layout is not None:
        raise ValueError("The 'layout' keyword is not supported when 'by' is None")

    if ax is None:
        rc = {"figure.figsize": figsize} if figsize is not None else {}
        with plt.rc_context(rc):
            ax = plt.gca()
    data = data._get_numeric_data()
    naxes = len(data.columns)
    if naxes == 0:
        raise ValueError(
            "boxplot method requires numerical columns, nothing to plot."
        )
    if columns is None:
        columns = data.columns
    else:
        data = data[columns]

    result = plot_group(columns, data.values.T, ax, **kwds)
    ax.grid(grid)

exit(result)
