# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py

if maybe_use_numba(engine):
    with self._group_selection_context():
        data = self._selected_obj
    result = self._aggregate_with_numba(
        data.to_frame(), func, *args, engine_kwargs=engine_kwargs, **kwargs
    )
    index = self.grouper.result_index
    result = self.obj._constructor(result.ravel(), index=index, name=data.name)
    if not self.as_index:
        result = self._insert_inaxis_grouper(result)
        result.index = default_index(len(result))
    exit(result)

relabeling = func is None
columns = None
if relabeling:
    columns, func = validate_func_kwargs(kwargs)
    kwargs = {}

if isinstance(func, str):
    exit(getattr(self, func)(*args, **kwargs))

elif isinstance(func, abc.Iterable):
    # Catch instances of lists / tuples
    # but not the class list / tuple itself.
    func = maybe_mangle_lambdas(func)
    ret = self._aggregate_multiple_funcs(func)
    if relabeling:
        # columns is not narrowed by mypy from relabeling flag
        assert columns is not None  # for mypy
        ret.columns = columns
    if not self.as_index:
        ret = self._insert_inaxis_grouper(ret)
        ret.index = default_index(len(ret))
    exit(ret)

else:
    cyfunc = com.get_cython_func(func)
    if cyfunc and not args and not kwargs:
        exit(getattr(self, cyfunc)())

    if self.grouper.nkeys > 1:
        exit(self._python_agg_general(func, *args, **kwargs))

    try:
        exit(self._python_agg_general(func, *args, **kwargs))
    except KeyError:
        # TODO: KeyError is raised in _python_agg_general,
        #  see test_groupby.test_basic
        result = self._aggregate_named(func, *args, **kwargs)

        # result is a dict whose keys are the elements of result_index
        index = self.grouper.result_index
        result = Series(result, index=index)
        if not self.as_index:
            result = self._insert_inaxis_grouper(result)
            result.index = default_index(len(result))
        exit(result)
