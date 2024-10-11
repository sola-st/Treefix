# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Converts the body function for all but last iteration."""
wrapped_inputs = [wrap(inp, stacked) for inp, stacked in
                  zip(new_inputs, inputs_stacked)]
# Note the iterative process below to figure out loop invariance.
# Here we iterate on vectorization process till a fixed point. The issue
# is that the while body can take pfor loop invariant inputs but return
# loop variant outputs. For any loop variant output, the corresponding
# input has to be then made loop variant (since subsequent while
# iterations will need to see loop variant values).
# However once we make a new input loop variant, we might make other
# outputs loop variant. Hence we need to iterate till we get fixed point.
while True:
    if self._pfor.all_indices_partitioned:
        indices = array_ops.gather(self._pfor.all_indices, new_indices)
    else:
        indices = new_indices
    body_pfor = PFor(
        loop_var=self._pfor.loop_var,
        loop_len=array_ops.size(new_indices),
        pfor_ops=self._body_func.graph.get_operations(),
        fallback_to_while_loop=self._pfor.fallback_to_while_loop,
        all_indices=indices,
        all_indices_partitioned=(self._pfor.all_indices_partitioned or
                                 cond_stacked),
        pfor_config=self._pfor.pfor_config)
    stacking_mismatch = False
    outputs = _convert_function_call(self._body_func,
                                     body_pfor,
                                     wrapped_inputs)
    for i, (out, inp) in enumerate(zip(outputs, wrapped_inputs)):
        if out.is_stacked != inp.is_stacked:
            stacking_mismatch = True
            mismatching_stacked_indices.append(i)
            stacked = _stack(inp.t, [array_ops.size(new_indices)])
            if inp.t.dtype == dtypes.variant:
                stacked = wrap(
                    _tile_variant_with_length(stacked.t,
                                              [array_ops.size(new_indices)]))
            wrapped_inputs[i] = stacked
    if not stacking_mismatch:
        if mismatching_stacked_indices:
            # We needed to stack some inputs. This code will be abandoned and
            # should not get executed. Hence we simply return `new_inputs` to
            # make sure the graph construction code completes.
            with ops.control_dependencies([
                control_flow_ops.Assert(
                    False, ["pfor ERROR: this branch should never execute"])]):
                exit([array_ops.identity(x) for x in new_inputs])
        else:
            exit([out.t for out in outputs])
