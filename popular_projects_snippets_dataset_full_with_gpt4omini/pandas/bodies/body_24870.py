# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
        Set the table styles included within the ``<style>`` HTML element.

        This function can be used to style the entire table, columns, rows or
        specific HTML selectors.

        Parameters
        ----------
        table_styles : list or dict
            If supplying a list, each individual table_style should be a
            dictionary with ``selector`` and ``props`` keys. ``selector``
            should be a CSS selector that the style will be applied to
            (automatically prefixed by the table's UUID) and ``props``
            should be a list of tuples with ``(attribute, value)``.
            If supplying a dict, the dict keys should correspond to
            column names or index values, depending upon the specified
            `axis` argument. These will be mapped to row or col CSS
            selectors. MultiIndex values as dict keys should be
            in their respective tuple form. The dict values should be
            a list as specified in the form with CSS selectors and
            props that will be applied to the specified row or column.

            .. versionchanged:: 1.2.0

        axis : {0 or 'index', 1 or 'columns', None}, default 0
            Apply to each column (``axis=0`` or ``'index'``), to each row
            (``axis=1`` or ``'columns'``). Only used if `table_styles` is
            dict.

            .. versionadded:: 1.2.0

        overwrite : bool, default True
            Styles are replaced if `True`, or extended if `False`. CSS
            rules are preserved so most recent styles set will dominate
            if selectors intersect.

            .. versionadded:: 1.2.0

        css_class_names : dict, optional
            A dict of strings used to replace the default CSS classes described below.

            .. versionadded:: 1.4.0

        Returns
        -------
        Styler

        See Also
        --------
        Styler.set_td_classes: Set the DataFrame of strings added to the ``class``
            attribute of ``<td>`` HTML elements.
        Styler.set_table_attributes: Set the table attributes added to the ``<table>``
            HTML element.

        Notes
        -----
        The default CSS classes dict, whose values can be replaced is as follows:

        .. code-block:: python

            css_class_names = {"row_heading": "row_heading",
                               "col_heading": "col_heading",
                               "index_name": "index_name",
                               "col": "col",
                               "row": "row",
                               "col_trim": "col_trim",
                               "row_trim": "row_trim",
                               "level": "level",
                               "data": "data",
                               "blank": "blank",
                               "foot": "foot"}

        Examples
        --------
        >>> df = pd.DataFrame(np.random.randn(10, 4),
        ...                   columns=['A', 'B', 'C', 'D'])
        >>> df.style.set_table_styles(
        ...     [{'selector': 'tr:hover',
        ...       'props': [('background-color', 'yellow')]}]
        ... )  # doctest: +SKIP

        Or with CSS strings

        >>> df.style.set_table_styles(
        ...     [{'selector': 'tr:hover',
        ...       'props': 'background-color: yellow; font-size: 1em;'}]
        ... )  # doctest: +SKIP

        Adding column styling by name

        >>> df.style.set_table_styles({
        ...     'A': [{'selector': '',
        ...            'props': [('color', 'red')]}],
        ...     'B': [{'selector': 'td',
        ...            'props': 'color: blue;'}]
        ... }, overwrite=False)  # doctest: +SKIP

        Adding row styling

        >>> df.style.set_table_styles({
        ...     0: [{'selector': 'td:hover',
        ...          'props': [('font-size', '25px')]}]
        ... }, axis=1, overwrite=False)  # doctest: +SKIP

        See `Table Visualization <../../user_guide/style.ipynb>`_ user guide for
        more details.
        """
if css_class_names is not None:
    self.css = {**self.css, **css_class_names}

if table_styles is None:
    exit(self)
elif isinstance(table_styles, dict):
    axis = self.data._get_axis_number(axis)
    obj = self.data.index if axis == 1 else self.data.columns
    idf = f".{self.css['row']}" if axis == 1 else f".{self.css['col']}"

    table_styles = [
        {
            "selector": str(s["selector"]) + idf + str(idx),
            "props": maybe_convert_css_to_tuples(s["props"]),
        }
        for key, styles in table_styles.items()
        for idx in obj.get_indexer_for([key])
        for s in format_table_styles(styles)
    ]
else:
    table_styles = [
        {
            "selector": s["selector"],
            "props": maybe_convert_css_to_tuples(s["props"]),
        }
        for s in table_styles
    ]

if not overwrite and self.table_styles is not None:
    self.table_styles.extend(table_styles)
else:
    self.table_styles = table_styles
exit(self)
