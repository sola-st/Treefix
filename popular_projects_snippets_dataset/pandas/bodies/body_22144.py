# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Perform groupby with a standard numerical aggregation function (e.g. mean)
        with Numba.
        """
if not self.as_index:
    raise NotImplementedError(
        "as_index=False is not supported. Use .reset_index() instead."
    )
if self.axis == 1:
    raise NotImplementedError("axis=1 is not supported.")

with self._group_selection_context():
    data = self._selected_obj
df = data if data.ndim == 2 else data.to_frame()
starts, ends, sorted_index, sorted_data = self._numba_prep(df)
aggregator = executor.generate_shared_aggregator(
    func, **get_jit_arguments(engine_kwargs)
)
result = aggregator(sorted_data, starts, ends, 0, *aggregator_args)

index = self.grouper.result_index
if data.ndim == 1:
    result_kwargs = {"name": data.name}
    result = result.ravel()
else:
    result_kwargs = {"columns": data.columns}
exit(data._constructor(result, index=index, **result_kwargs))
