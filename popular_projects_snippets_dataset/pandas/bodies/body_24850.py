# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
        Set the ``class`` attribute of ``<td>`` HTML elements.

        Parameters
        ----------
        classes : DataFrame
            DataFrame containing strings that will be translated to CSS classes,
            mapped by identical column and index key values that must exist on the
            underlying Styler data. None, NaN values, and empty strings will
            be ignored and not affect the rendered HTML.

        Returns
        -------
        Styler

        See Also
        --------
        Styler.set_table_styles: Set the table styles included within the ``<style>``
            HTML element.
        Styler.set_table_attributes: Set the table attributes added to the ``<table>``
            HTML element.

        Notes
        -----
        Can be used in combination with ``Styler.set_table_styles`` to define an
        internal CSS solution without reference to external CSS files.

        Examples
        --------
        >>> df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=["A", "B", "C"])
        >>> classes = pd.DataFrame([
        ...     ["min-val red", "", "blue"],
        ...     ["red", None, "blue max-val"]
        ... ], index=df.index, columns=df.columns)
        >>> df.style.set_td_classes(classes)  # doctest: +SKIP

        Using `MultiIndex` columns and a `classes` `DataFrame` as a subset of the
        underlying,

        >>> df = pd.DataFrame([[1,2],[3,4]], index=["a", "b"],
        ...     columns=[["level0", "level0"], ["level1a", "level1b"]])
        >>> classes = pd.DataFrame(["min-val"], index=["a"],
        ...     columns=[["level0"],["level1a"]])
        >>> df.style.set_td_classes(classes)  # doctest: +SKIP

        Form of the output with new additional css classes,

        >>> df = pd.DataFrame([[1]])
        >>> css = pd.DataFrame([["other-class"]])
        >>> s = Styler(df, uuid="_", cell_ids=False).set_td_classes(css)
        >>> s.hide(axis=0).to_html()  # doctest: +SKIP
        '<style type="text/css"></style>'
        '<table id="T__">'
        '  <thead>'
        '    <tr><th class="col_heading level0 col0" >0</th></tr>'
        '  </thead>'
        '  <tbody>'
        '    <tr><td class="data row0 col0 other-class" >1</td></tr>'
        '  </tbody>'
        '</table>'
        """
if not classes.index.is_unique or not classes.columns.is_unique:
    raise KeyError(
        "Classes render only if `classes` has unique index and columns."
    )
classes = classes.reindex_like(self.data)

for r, row_tup in enumerate(classes.itertuples()):
    for c, value in enumerate(row_tup[1:]):
        if not (pd.isna(value) or value == ""):
            self.cell_context[(r, c)] = str(value)

exit(self)
