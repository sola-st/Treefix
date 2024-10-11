# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
r"""
        Format the text display value of index labels or column headers.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        formatter : str, callable, dict or None
            Object to define how values are displayed. See notes.
        axis : {0, "index", 1, "columns"}
            Whether to apply the formatter to the index or column headers.
        level : int, str, list
            The level(s) over which to apply the generic formatter.
        na_rep : str, optional
            Representation for missing values.
            If ``na_rep`` is None, no special formatting is applied.
        precision : int, optional
            Floating point precision to use for display purposes, if not determined by
            the specified ``formatter``.
        decimal : str, default "."
            Character used as decimal separator for floats, complex and integers.
        thousands : str, optional, default None
            Character used as thousands separator for floats, complex and integers.
        escape : str, optional
            Use 'html' to replace the characters ``&``, ``<``, ``>``, ``'``, and ``"``
            in cell display string with HTML-safe sequences.
            Use 'latex' to replace the characters ``&``, ``%``, ``$``, ``#``, ``_``,
            ``{``, ``}``, ``~``, ``^``, and ``\`` in the cell display string with
            LaTeX-safe sequences.
            Escaping is done before ``formatter``.
        hyperlinks : {"html", "latex"}, optional
            Convert string patterns containing https://, http://, ftp:// or www. to
            HTML <a> tags as clickable URL hyperlinks if "html", or LaTeX \href
            commands if "latex".

        Returns
        -------
        Styler

        See Also
        --------
        Styler.format: Format the text display value of data cells.

        Notes
        -----
        This method assigns a formatting function, ``formatter``, to each level label
        in the DataFrame's index or column headers. If ``formatter`` is ``None``,
        then the default formatter is used.
        If a callable then that function should take a label value as input and return
        a displayable representation, such as a string. If ``formatter`` is
        given as a string this is assumed to be a valid Python format specification
        and is wrapped to a callable as ``string.format(x)``. If a ``dict`` is given,
        keys should correspond to MultiIndex level numbers or names, and values should
        be string or callable, as above.

        The default formatter currently expresses floats and complex numbers with the
        pandas display precision unless using the ``precision`` argument here. The
        default formatter does not adjust the representation of missing values unless
        the ``na_rep`` argument is used.

        The ``level`` argument defines which levels of a MultiIndex to apply the
        method to. If the ``formatter`` argument is given in dict form but does
        not include all levels within the level argument then these unspecified levels
        will have the default formatter applied. Any levels in the formatter dict
        specifically excluded from the level argument will be ignored.

        When using a ``formatter`` string the dtypes must be compatible, otherwise a
        `ValueError` will be raised.

        .. warning::
           `Styler.format_index` is ignored when using the output format
           `Styler.to_excel`, since Excel and Python have inherrently different
           formatting structures.
           However, it is possible to use the `number-format` pseudo CSS attribute
           to force Excel permissible formatting. See documentation for `Styler.format`.

        Examples
        --------
        Using ``na_rep`` and ``precision`` with the default ``formatter``

        >>> df = pd.DataFrame([[1, 2, 3]], columns=[2.0, np.nan, 4.0])
        >>> df.style.format_index(axis=1, na_rep='MISS', precision=3)  # doctest: +SKIP
            2.000    MISS   4.000
        0       1       2       3

        Using a ``formatter`` specification on consistent dtypes in a level

        >>> df.style.format_index('{:.2f}', axis=1, na_rep='MISS')  # doctest: +SKIP
             2.00   MISS    4.00
        0       1      2       3

        Using the default ``formatter`` for unspecified levels

        >>> df = pd.DataFrame([[1, 2, 3]],
        ...     columns=pd.MultiIndex.from_arrays([["a", "a", "b"],[2, np.nan, 4]]))
        >>> df.style.format_index({0: lambda v: upper(v)}, axis=1, precision=1)
        ...  # doctest: +SKIP
                       A       B
              2.0    nan     4.0
        0       1      2       3

        Using a callable ``formatter`` function.

        >>> func = lambda s: 'STRING' if isinstance(s, str) else 'FLOAT'
        >>> df.style.format_index(func, axis=1, na_rep='MISS')
        ...  # doctest: +SKIP
                  STRING  STRING
            FLOAT   MISS   FLOAT
        0       1      2       3

        Using a ``formatter`` with HTML ``escape`` and ``na_rep``.

        >>> df = pd.DataFrame([[1, 2, 3]], columns=['"A"', 'A&B', None])
        >>> s = df.style.format_index('$ {0}', axis=1, escape="html", na_rep="NA")
        ...  # doctest: +SKIP
        <th .. >$ &#34;A&#34;</th>
        <th .. >$ A&amp;B</th>
        <th .. >NA</td>
        ...

        Using a ``formatter`` with LaTeX ``escape``.

        >>> df = pd.DataFrame([[1, 2, 3]], columns=["123", "~", "$%#"])
        >>> df.style.format_index("\\textbf{{{}}}", escape="latex", axis=1).to_latex()
        ...  # doctest: +SKIP
        \begin{tabular}{lrrr}
        {} & {\textbf{123}} & {\textbf{\textasciitilde }} & {\textbf{\$\%\#}} \\
        0 & 1 & 2 & 3 \\
        \end{tabular}
        """
axis = self.data._get_axis_number(axis)
if axis == 0:
    display_funcs_, obj = self._display_funcs_index, self.index
else:
    display_funcs_, obj = self._display_funcs_columns, self.columns
levels_ = refactor_levels(level, obj)

if all(
    (
        formatter is None,
        level is None,
        precision is None,
        decimal == ".",
        thousands is None,
        na_rep is None,
        escape is None,
        hyperlinks is None,
    )
):
    display_funcs_.clear()
    exit(self)  # clear the formatter / revert to default and avoid looping

if not isinstance(formatter, dict):
    formatter = {level: formatter for level in levels_}
else:
    formatter = {
        obj._get_level_number(level): formatter_
        for level, formatter_ in formatter.items()
    }

for lvl in levels_:
    format_func = _maybe_wrap_formatter(
        formatter.get(lvl),
        na_rep=na_rep,
        precision=precision,
        decimal=decimal,
        thousands=thousands,
        escape=escape,
        hyperlinks=hyperlinks,
    )

    for idx in [(i, lvl) if axis == 0 else (lvl, i) for i in range(len(obj))]:
        display_funcs_[idx] = format_func

exit(self)
