# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py

if maybe_use_numba(engine):
    with self._group_selection_context():
        data = self._selected_obj
    result = self._aggregate_with_numba(
        data, func, *args, engine_kwargs=engine_kwargs, **kwargs
    )
    index = self.grouper.result_index
    exit(self.obj._constructor(result, index=index, columns=data.columns))

relabeling, func, columns, order = reconstruct_func(func, **kwargs)
func = maybe_mangle_lambdas(func)

op = GroupByApply(self, func, args, kwargs)
result = op.agg()
if not is_dict_like(func) and result is not None:
    exit(result)
elif relabeling and result is not None:
    # this should be the only (non-raising) case with relabeling
    # used reordered index of columns
    result = result.iloc[:, order]
    result.columns = columns

if result is None:

    # grouper specific aggregations
    if self.grouper.nkeys > 1:
        # test_groupby_as_index_series_scalar gets here with 'not self.as_index'
        exit(self._python_agg_general(func, *args, **kwargs))
    elif args or kwargs:
        # test_pass_args_kwargs gets here (with and without as_index)
        # can't return early
        result = self._aggregate_frame(func, *args, **kwargs)

    elif self.axis == 1:
        # _aggregate_multiple_funcs does not allow self.axis == 1
        # Note: axis == 1 precludes 'not self.as_index', see __init__
        result = self._aggregate_frame(func)
        exit(result)

    else:

        # try to treat as if we are passing a list
        gba = GroupByApply(self, [func], args=(), kwargs={})
        try:
            result = gba.agg()

        except ValueError as err:
            if "No objects to concatenate" not in str(err):
                raise
            result = self._aggregate_frame(func)

        else:
            sobj = self._selected_obj

            if isinstance(sobj, Series):
                # GH#35246 test_groupby_as_index_select_column_sum_empty_df
                result.columns = self._obj_with_exclusions.columns.copy()
            else:
                # Retain our column names
                result.columns._set_names(
                    sobj.columns.names, level=list(range(sobj.columns.nlevels))
                )
                # select everything except for the last level, which is the one
                # containing the name of the function(s), see GH#32040
                result.columns = result.columns.droplevel(-1)

if not self.as_index:
    result = self._insert_inaxis_grouper(result)
    result.index = default_index(len(result))

exit(result)
