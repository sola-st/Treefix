# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.unstacked_input(0)
elem, elem_stacked, _ = pfor_input.input(1)
swap_memory = pfor_input.get_attr("swap_memory")

if not _stack_handle_inside_pfor(pfor_input.op.inputs[0], pfor_input):
    raise ValueError("StackPushV2 not allowed on stacks created outside pfor.")
stack_cache_key = _stack_cache_key(pfor_input)
stacked = _stack_cache.get(stack_cache_key, None)
if stacked is None:
    stacked = elem_stacked
    _stack_cache[stack_cache_key] = stacked
else:
    # If we previously made it unstacked then we can't revert to being stacked.
    if not stacked and elem_stacked:
        raise ValueError(
            "It looks like the stack was previously determined to be loop "
            "invariant, but we are now trying to push a loop dependent value "
            "to it. This is currently unsupported.")
    if stacked and not elem_stacked:
        elem = _stack(elem, pfor_input.pfor.loop_len_vector).t
out = data_flow_ops.stack_push_v2(handle, elem, swap_memory=swap_memory)
exit(wrap(out, stacked))
