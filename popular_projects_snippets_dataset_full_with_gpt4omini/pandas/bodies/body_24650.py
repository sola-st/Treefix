# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
r"""
        Format the text display value of cells.

        Parameters
        ----------
        formatter : str, callable, dict or None
            Object to define how values are displayed. See notes.
        subset : label, array-like, IndexSlice, optional
            A valid 2d input to `DataFrame.loc[<subset>]`, or, in the case of a 1d input
            or single key, to `DataFrame.loc[:, <subset>]` where the columns are
            prioritised, to limit ``data`` to *before* applying the function.
        na_rep : str, optional
            Representation for missing values.
            If ``na_rep`` is None, no special formatting is applied.

            .. versionadded:: 1.0.0

        precision : int, optional
            Floating point precision to use for display purposes, if not determined by
            the specified ``formatter``.

            .. versionadded:: 1.3.0

        decimal : str, default "."
            Character used as decimal separator for floats, complex and integers.

            .. versionadded:: 1.3.0

        thousands : str, optional, default None
            Character used as thousands separator for floats, complex and integers.

            .. versionadded:: 1.3.0

        escape : str, optional
            Use 'html' to replace the characters ``&``, ``<``, ``>``, ``'``, and ``"``
            in cell display string with HTML-safe sequences.
            Use 'latex' to replace the characters ``&``, ``%``, ``$``, ``#``, ``_``,
            ``{``, ``}``, ``~``, ``^``, and ``\`` in the cell display string with
            LaTeX-safe sequences.
            Escaping is done before ``formatter``.

            .. versionadded:: 1.3.0

        hyperlinks : {"html", "latex"}, optional
            Convert string patterns containing https://, http://, ftp:// or www. to
            HTML <a> tags as clickable URL hyperlinks if "html", or LaTeX \href
            commands if "latex".

            .. versionadded:: 1.4.0

        Returns
        -------
        Styler

        See Also
        --------
        Styler.format_index: Format the text display value of index labels.

        Notes
        -----
        This method assigns a formatting function, ``formatter``, to each cell in the
        DataFrame. If ``formatter`` is ``None``, then the default formatter is used.
        If a callable then that function should take a data value as input and return
        a displayable representation, such as a string. If ``formatter`` is
        given as a string this is assumed to be a valid Python format specification
        and is wrapped to a callable as ``string.format(x)``. If a ``dict`` is given,
        keys should correspond to column names, and values should be string or
        callable, as above.

        The default formatter currently expresses floats and complex numbers with the
        pandas display precision unless using the ``precision`` argument here. The
        default formatter does not adjust the representation of missing values unless
        the ``na_rep`` argument is used.

        The ``subset`` argument defines which region to apply the formatting function
        to. If the ``formatter`` argument is given in dict form but does not include
        all columns within the subset then these columns will have the default formatter
        applied. Any columns in the formatter dict excluded from the subset will
        be ignored.

        When using a ``formatter`` string the dtypes must be compatible, otherwise a
        `ValueError` will be raised.

        When instantiating a Styler, default formatting can be applied be setting the
        ``pandas.options``:

          - ``styler.format.formatter``: default None.
          - ``styler.format.na_rep``: default None.
          - ``styler.format.precision``: default 6.
          - ``styler.format.decimal``: default ".".
          - ``styler.format.thousands``: default None.
          - ``styler.format.escape``: default None.

        .. warning::
           `Styler.format` is ignored when using the output format `Styler.to_excel`,
           since Excel and Python have inherrently different formatting structures.
           However, it is possible to use the `number-format` pseudo CSS attribute
           to force Excel permissible formatting. See examples.

        Examples
        --------
        Using ``na_rep`` and ``precision`` with the default ``formatter``

        >>> df = pd.DataFrame([[np.nan, 1.0, 'A'], [2.0, np.nan, 3.0]])
        >>> df.style.format(na_rep='MISS', precision=3)  # doctest: +SKIP
                0       1       2
        0    MISS   1.000       A
        1   2.000    MISS   3.000

        Using a ``formatter`` specification on consistent column dtypes

        >>> df.style.format('{:.2f}', na_rep='MISS', subset=[0,1])  # doctest: +SKIP
                0      1          2
        0    MISS   1.00          A
        1    2.00   MISS   3.000000

        Using the default ``formatter`` for unspecified columns

        >>> df.style.format({0: '{:.2f}', 1: '£ {:.1f}'}, na_rep='MISS', precision=1)
        ...  # doctest: +SKIP
                 0      1     2
        0    MISS   £ 1.0     A
        1    2.00    MISS   3.0

        Multiple ``na_rep`` or ``precision`` specifications under the default
        ``formatter``.

        >>> df.style.format(na_rep='MISS', precision=1, subset=[0])
        ...     .format(na_rep='PASS', precision=2, subset=[1, 2])  # doctest: +SKIP
                0      1      2
        0    MISS   1.00      A
        1     2.0   PASS   3.00

        Using a callable ``formatter`` function.

        >>> func = lambda s: 'STRING' if isinstance(s, str) else 'FLOAT'
        >>> df.style.format({0: '{:.1f}', 2: func}, precision=4, na_rep='MISS')
        ...  # doctest: +SKIP
                0        1        2
        0    MISS   1.0000   STRING
        1     2.0     MISS    FLOAT

        Using a ``formatter`` with HTML ``escape`` and ``na_rep``.

        >>> df = pd.DataFrame([['<div></div>', '"A&B"', None]])
        >>> s = df.style.format(
        ...     '<a href="a.com/{0}">{0}</a>', escape="html", na_rep="NA"
        ...     )
        >>> s.to_html()  # doctest: +SKIP
        ...
        <td .. ><a href="a.com/&lt;div&gt;&lt;/div&gt;">&lt;div&gt;&lt;/div&gt;</a></td>
        <td .. ><a href="a.com/&#34;A&amp;B&#34;">&#34;A&amp;B&#34;</a></td>
        <td .. >NA</td>
        ...

        Using a ``formatter`` with LaTeX ``escape``.

        >>> df = pd.DataFrame([["123"], ["~ ^"], ["$%#"]])
        >>> df.style.format("\\textbf{{{}}}", escape="latex").to_latex()
        ...  # doctest: +SKIP
        \begin{tabular}{ll}
        {} & {0} \\
        0 & \textbf{123} \\
        1 & \textbf{\textasciitilde \space \textasciicircum } \\
        2 & \textbf{\$\%\#} \\
        \end{tabular}

        Pandas defines a `number-format` pseudo CSS attribute instead of the `.format`
        method to create `to_excel` permissible formatting. Note that semi-colons are
        CSS protected characters but used as separators in Excel's format string.
        Replace semi-colons with the section separator character (ASCII-245) when
        defining the formatting here.

        >>> df = pd.DataFrame({"A": [1, 0, -1]})
        >>> pseudo_css = "number-format: 0§[Red](0)§-§@;"
        >>> filename = "formatted_file.xlsx"
        >>> df.style.applymap(lambda v: pseudo_css).to_excel(filename) # doctest: +SKIP

        .. figure:: ../../_static/style/format_excel_css.png
        """
if all(
    (
        formatter is None,
        subset is None,
        precision is None,
        decimal == ".",
        thousands is None,
        na_rep is None,
        escape is None,
        hyperlinks is None,
    )
):
    self._display_funcs.clear()
    exit(self)  # clear the formatter / revert to default and avoid looping

subset = slice(None) if subset is None else subset
subset = non_reducing_slice(subset)
data = self.data.loc[subset]

if not isinstance(formatter, dict):
    formatter = {col: formatter for col in data.columns}

cis = self.columns.get_indexer_for(data.columns)
ris = self.index.get_indexer_for(data.index)
for ci in cis:
    format_func = _maybe_wrap_formatter(
        formatter.get(self.columns[ci]),
        na_rep=na_rep,
        precision=precision,
        decimal=decimal,
        thousands=thousands,
        escape=escape,
        hyperlinks=hyperlinks,
    )
    for ri in ris:
        self._display_funcs[(ri, ci)] = format_func

exit(self)
