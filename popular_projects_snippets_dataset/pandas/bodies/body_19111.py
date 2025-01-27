# Extracted from ./data/repos/pandas/pandas/core/computation/align.py
term_index = [i for i, term in enumerate(terms) if hasattr(term.value, "axes")]
term_dims = [terms[i].value.ndim for i in term_index]

from pandas import Series

ndims = Series(dict(zip(term_index, term_dims)))

# initial axes are the axes of the largest-axis'd term
biggest = terms[ndims.idxmax()].value
typ = biggest._constructor
axes = biggest.axes
naxes = len(axes)
gt_than_one_axis = naxes > 1

for value in (terms[i].value for i in term_index):
    is_series = isinstance(value, ABCSeries)
    is_series_and_gt_one_axis = is_series and gt_than_one_axis

    for axis, items in enumerate(value.axes):
        if is_series_and_gt_one_axis:
            ax, itm = naxes - 1, value.index
        else:
            ax, itm = axis, items

        if not axes[ax].is_(itm):
            axes[ax] = axes[ax].join(itm, how="outer")

for i, ndim in ndims.items():
    for axis, items in zip(range(ndim), axes):
        ti = terms[i].value

        if hasattr(ti, "reindex"):
            transpose = isinstance(ti, ABCSeries) and naxes > 1
            reindexer = axes[naxes - 1] if transpose else items

            term_axis_size = len(ti.axes[axis])
            reindexer_size = len(reindexer)

            ordm = np.log10(max(1, abs(reindexer_size - term_axis_size)))
            if ordm >= 1 and reindexer_size >= 10000:
                w = (
                    f"Alignment difference on axis {axis} is larger "
                    f"than an order of magnitude on term {repr(terms[i].name)}, "
                    f"by more than {ordm:.4g}; performance may suffer."
                )
                warnings.warn(
                    w, category=PerformanceWarning, stacklevel=find_stack_level()
                )

            f = partial(ti.reindex, reindexer, axis=axis, copy=False)

            terms[i].update(f())

    terms[i].update(terms[i].value.values)

exit((typ, _zip_axes_from_type(typ, axes)))
