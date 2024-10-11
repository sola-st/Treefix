# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Reset the index, or a level of it.

        Reset the index of the DataFrame, and use the default one instead.
        If the DataFrame has a MultiIndex, this method can remove one or more
        levels.

        Parameters
        ----------
        level : int, str, tuple, or list, default None
            Only remove the given levels from the index. Removes all levels by
            default.
        drop : bool, default False
            Do not try to insert index into dataframe columns. This resets
            the index to the default integer index.
        inplace : bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        col_level : int or str, default 0
            If the columns have multiple levels, determines which level the
            labels are inserted into. By default it is inserted into the first
            level.
        col_fill : object, default ''
            If the columns have multiple levels, determines how the other
            levels are named. If None then the index name is repeated.
        allow_duplicates : bool, optional, default lib.no_default
            Allow duplicate column labels to be created.

            .. versionadded:: 1.5.0

        names : int, str or 1-dimensional list, default None
            Using the given string, rename the DataFrame column which contains the
            index data. If the DataFrame has a MultiIndex, this has to be a list or
            tuple with length equal to the number of levels.

            .. versionadded:: 1.5.0

        Returns
        -------
        DataFrame or None
            DataFrame with the new index or None if ``inplace=True``.

        See Also
        --------
        DataFrame.set_index : Opposite of reset_index.
        DataFrame.reindex : Change to new indices or expand indices.
        DataFrame.reindex_like : Change to same indices as other DataFrame.

        Examples
        --------
        >>> df = pd.DataFrame([('bird', 389.0),
        ...                    ('bird', 24.0),
        ...                    ('mammal', 80.5),
        ...                    ('mammal', np.nan)],
        ...                   index=['falcon', 'parrot', 'lion', 'monkey'],
        ...                   columns=('class', 'max_speed'))
        >>> df
                 class  max_speed
        falcon    bird      389.0
        parrot    bird       24.0
        lion    mammal       80.5
        monkey  mammal        NaN

        When we reset the index, the old index is added as a column, and a
        new sequential index is used:

        >>> df.reset_index()
            index   class  max_speed
        0  falcon    bird      389.0
        1  parrot    bird       24.0
        2    lion  mammal       80.5
        3  monkey  mammal        NaN

        We can use the `drop` parameter to avoid the old index being added as
        a column:

        >>> df.reset_index(drop=True)
            class  max_speed
        0    bird      389.0
        1    bird       24.0
        2  mammal       80.5
        3  mammal        NaN

        You can also use `reset_index` with `MultiIndex`.

        >>> index = pd.MultiIndex.from_tuples([('bird', 'falcon'),
        ...                                    ('bird', 'parrot'),
        ...                                    ('mammal', 'lion'),
        ...                                    ('mammal', 'monkey')],
        ...                                   names=['class', 'name'])
        >>> columns = pd.MultiIndex.from_tuples([('speed', 'max'),
        ...                                      ('species', 'type')])
        >>> df = pd.DataFrame([(389.0, 'fly'),
        ...                    (24.0, 'fly'),
        ...                    (80.5, 'run'),
        ...                    (np.nan, 'jump')],
        ...                   index=index,
        ...                   columns=columns)
        >>> df
                       speed species
                         max    type
        class  name
        bird   falcon  389.0     fly
               parrot   24.0     fly
        mammal lion     80.5     run
               monkey    NaN    jump

        Using the `names` parameter, choose a name for the index column:

        >>> df.reset_index(names=['classes', 'names'])
          classes   names  speed species
                             max    type
        0    bird  falcon  389.0     fly
        1    bird  parrot   24.0     fly
        2  mammal    lion   80.5     run
        3  mammal  monkey    NaN    jump

        If the index has multiple levels, we can reset a subset of them:

        >>> df.reset_index(level='class')
                 class  speed species
                          max    type
        name
        falcon    bird  389.0     fly
        parrot    bird   24.0     fly
        lion    mammal   80.5     run
        monkey  mammal    NaN    jump

        If we are not dropping the index, by default, it is placed in the top
        level. We can place it in another level:

        >>> df.reset_index(level='class', col_level=1)
                        speed species
                 class    max    type
        name
        falcon    bird  389.0     fly
        parrot    bird   24.0     fly
        lion    mammal   80.5     run
        monkey  mammal    NaN    jump

        When the index is inserted under another level, we can specify under
        which one with the parameter `col_fill`:

        >>> df.reset_index(level='class', col_level=1, col_fill='species')
                      species  speed species
                        class    max    type
        name
        falcon           bird  389.0     fly
        parrot           bird   24.0     fly
        lion           mammal   80.5     run
        monkey         mammal    NaN    jump

        If we specify a nonexistent level for `col_fill`, it is created:

        >>> df.reset_index(level='class', col_level=1, col_fill='genus')
                        genus  speed species
                        class    max    type
        name
        falcon           bird  389.0     fly
        parrot           bird   24.0     fly
        lion           mammal   80.5     run
        monkey         mammal    NaN    jump
        """
inplace = validate_bool_kwarg(inplace, "inplace")
self._check_inplace_and_allows_duplicate_labels(inplace)
if inplace:
    new_obj = self
else:
    new_obj = self.copy(deep=None)
if allow_duplicates is not lib.no_default:
    allow_duplicates = validate_bool_kwarg(allow_duplicates, "allow_duplicates")

new_index = default_index(len(new_obj))
if level is not None:
    if not isinstance(level, (tuple, list)):
        level = [level]
    level = [self.index._get_level_number(lev) for lev in level]
    if len(level) < self.index.nlevels:
        new_index = self.index.droplevel(level)

if not drop:
    to_insert: Iterable[tuple[Any, Any | None]]

    default = "index" if "index" not in self else "level_0"
    names = self.index._get_default_index_names(names, default)

    if isinstance(self.index, MultiIndex):
        to_insert = zip(self.index.levels, self.index.codes)
    else:
        to_insert = ((self.index, None),)

    multi_col = isinstance(self.columns, MultiIndex)
    for i, (lev, lab) in reversed(list(enumerate(to_insert))):
        if level is not None and i not in level:
            continue
        name = names[i]
        if multi_col:
            col_name = list(name) if isinstance(name, tuple) else [name]
            if col_fill is None:
                if len(col_name) not in (1, self.columns.nlevels):
                    raise ValueError(
                        "col_fill=None is incompatible "
                        f"with incomplete column name {name}"
                    )
                col_fill = col_name[0]

            lev_num = self.columns._get_level_number(col_level)
            name_lst = [col_fill] * lev_num + col_name
            missing = self.columns.nlevels - len(name_lst)
            name_lst += [col_fill] * missing
            name = tuple(name_lst)

        # to ndarray and maybe infer different dtype
        level_values = lev._values
        if level_values.dtype == np.object_:
            level_values = lib.maybe_convert_objects(level_values)

        if lab is not None:
            # if we have the codes, extract the values with a mask
            level_values = algorithms.take(
                level_values, lab, allow_fill=True, fill_value=lev._na_value
            )

        new_obj.insert(
            0,
            name,
            level_values,
            allow_duplicates=allow_duplicates,
        )

new_obj.index = new_index
if not inplace:
    exit(new_obj)

exit(None)
