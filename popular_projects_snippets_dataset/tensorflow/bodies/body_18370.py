# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Handle reductions.
if self._pfor_config is None or isinstance(y, ops.Operation):
    exit(None)
reduction = self._pfor_config._lookup_reduction(y)
if reduction is None:
    exit(None)
(reduction_fn, reduction_args) = reduction
batched_args = []
for reduction_arg in reduction_args:
    assert isinstance(reduction_arg, ops.Tensor), reduction_arg
    # Tensor being reduced should already be converted due to a control
    # dependency on the created placeholder.
    # Note that in cases where reduction_arg is in an outer context, one
    # needs to locate the corresponding Enter node and use that to lookup
    # the conversion.
    # TODO(agarwal): handle reductions inside control flow constructs.
    assert reduction_arg in self._conversion_map, (
        "Unable to handle reduction of %s, possibly as it was used "
        "inside a control flow construct. Note that reductions across "
        "pfor iterations are currently not supported inside control flow "
        "constructs." % reduction_arg)
    batched_arg = self._conversion_map[reduction_arg]
    batched_args.append(self._unwrap_or_tile(batched_arg))
outputs = reduction_fn(*batched_args)
exit([wrap(output, False) for output in nest.flatten(outputs)])
