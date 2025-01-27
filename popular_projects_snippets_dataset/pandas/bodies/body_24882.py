# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
        Highlight values defined by a quantile with a style.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        %(subset)s
        %(color)s
        axis : {0 or 'index', 1 or 'columns', None}, default 0
            Axis along which to determine and highlight quantiles. If ``None`` quantiles
            are measured over the entire DataFrame. See examples.
        q_left : float, default 0
            Left bound, in [0, q_right), for the target quantile range.
        q_right : float, default 1
            Right bound, in (q_left, 1], for the target quantile range.
        interpolation : {‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}
            Argument passed to ``Series.quantile`` or ``DataFrame.quantile`` for
            quantile estimation.
        inclusive : {'both', 'neither', 'left', 'right'}
            Identify whether quantile bounds are closed or open.
        %(props)s

        Returns
        -------
        Styler

        See Also
        --------
        Styler.highlight_null: Highlight missing values with a style.
        Styler.highlight_max: Highlight the maximum with a style.
        Styler.highlight_min: Highlight the minimum with a style.
        Styler.highlight_between: Highlight a defined range with a style.

        Notes
        -----
        This function does not work with ``str`` dtypes.

        Examples
        --------
        Using ``axis=None`` and apply a quantile to all collective data

        >>> df = pd.DataFrame(np.arange(10).reshape(2,5) + 1)
        >>> df.style.highlight_quantile(axis=None, q_left=0.8, color="#fffd75")
        ...  # doctest: +SKIP

        .. figure:: ../../_static/style/hq_axNone.png

        Or highlight quantiles row-wise or column-wise, in this case by row-wise

        >>> df.style.highlight_quantile(axis=1, q_left=0.8, color="#fffd75")
        ...  # doctest: +SKIP

        .. figure:: ../../_static/style/hq_ax1.png

        Use ``props`` instead of default background coloring

        >>> df.style.highlight_quantile(axis=None, q_left=0.2, q_right=0.8,
        ...     props='font-weight:bold;color:#e83e8c')  # doctest: +SKIP

        .. figure:: ../../_static/style/hq_props.png
        """
subset_ = slice(None) if subset is None else subset
subset_ = non_reducing_slice(subset_)
data = self.data.loc[subset_]

# after quantile is found along axis, e.g. along rows,
# applying the calculated quantile to alternate axis, e.g. to each column
quantiles = [q_left, q_right]
if axis is None:
    q = Series(data.to_numpy().ravel()).quantile(
        q=quantiles, interpolation=interpolation
    )
    axis_apply: int | None = None
else:
    axis = self.data._get_axis_number(axis)
    q = data.quantile(
        axis=axis, numeric_only=False, q=quantiles, interpolation=interpolation
    )
    axis_apply = 1 - axis

if props is None:
    props = f"background-color: {color};"
exit(self.apply(
    _highlight_between,
    axis=axis_apply,
    subset=subset,
    props=props,
    left=q.iloc[0],
    right=q.iloc[1],
    inclusive=inclusive,
))
