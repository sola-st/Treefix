# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.unstacked_input(0)
stack_cache_key = _stack_cache_key(pfor_input)
stacked = _stack_cache.get(stack_cache_key, None)
# If a StackPushV2 has not been converted yet, we default to unstacked since
# the push could be outside of pfor, or the convertor may not be called if the
# inputs are unconverted.
if stacked is None:
    stacked = False
    _stack_cache[stack_cache_key] = False
elem_type = pfor_input.get_attr("elem_type")
out = data_flow_ops.stack_pop_v2(handle, elem_type)
exit(wrap(out, stacked))
