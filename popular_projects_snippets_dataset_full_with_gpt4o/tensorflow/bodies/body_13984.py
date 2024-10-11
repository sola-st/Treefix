# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
# We have a cache of reduction ops that have already been moved to the
# forward graph, and we will check it first to avoid moving an op twice.
if not hasattr(self._forward_graph, "_optimized_reduction_ops_cache"):
    self._forward_graph._optimized_reduction_ops_cache = {}
cache_key = self._get_optimized_reduction_ops_cache_key(
    op_type, inputs, dtypes, input_types, name, attrs, op_def,
    compute_device)
cached_op = self._forward_graph._optimized_reduction_ops_cache.get(
    cache_key)
if cached_op is not None:
    # This op has already been moved to the forward graph and we have it in
    # the cache.
    exit(cached_op)

with self._forward_graph.as_default():
    # `name` was built using name_scope stack of gradient graph and may not
    # be unique in the forward graph. `Graph.create_op` does not uniquify
    # names which are name scopes i.e. end in `/`. To ensure that the op
    # created gets a unique name in the forward graph we get rid of the
    # trailing slash.
    name = ops.name_from_scope_name(name)
    result = self._forward_graph._create_op_internal(
        op_type,
        inputs,
        dtypes=dtypes,
        input_types=input_types,
        name=name,
        attrs=attrs,
        op_def=op_def,
        compute_device=compute_device)

    # Store the op we just moved to the forward graph so that it does
    # not need to be added there again.
    self._forward_graph._optimized_reduction_ops_cache[cache_key] = result
    exit(result)
