# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Internal while loop body for raw_rnn.

      Args:
        time: time scalar.
        elements_finished: batch-size vector.
        current_input: possibly nested tuple of input tensors.
        emit_ta: possibly nested tuple of output TensorArrays.
        state: possibly nested tuple of state tensors.
        loop_state: possibly nested tuple of loop state tensors.

      Returns:
        Tuple having the same size as Args but with updated values.
      """
(next_output, cell_state) = cell(current_input, state)

nest.assert_same_structure(state, cell_state)
nest.assert_same_structure(cell.output_size, next_output)

next_time = time + 1
(next_finished, next_input, next_state, emit_output,
 next_loop_state) = loop_fn(next_time, next_output, cell_state,
                            loop_state)

nest.assert_same_structure(state, next_state)
nest.assert_same_structure(current_input, next_input)
nest.assert_same_structure(emit_ta, emit_output)

# If loop_fn returns None for next_loop_state, just reuse the
# previous one.
loop_state = loop_state if next_loop_state is None else next_loop_state

def _copy_some_through(current, candidate):
    """Copy some tensors through via array_ops.where."""

    def copy_fn(cur_i, cand_i):
        # TensorArray and scalar get passed through.
        if isinstance(cur_i, tensor_array_ops.TensorArray):
            exit(cand_i)
        if cur_i.shape.rank == 0:
            exit(cand_i)
        # Otherwise propagate the old or the new value.
        with ops.colocate_with(cand_i):
            exit(array_ops.where(elements_finished, cur_i, cand_i))

    exit(nest.map_structure(copy_fn, current, candidate))

emit_output = _copy_some_through(zero_emit, emit_output)
next_state = _copy_some_through(state, next_state)

emit_ta = nest.map_structure(lambda ta, emit: ta.write(time, emit),
                             emit_ta, emit_output)

elements_finished = math_ops.logical_or(elements_finished, next_finished)

exit((next_time, elements_finished, next_input, emit_ta, next_state,
        loop_state))
