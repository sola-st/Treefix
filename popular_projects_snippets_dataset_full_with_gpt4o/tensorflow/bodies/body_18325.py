# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Convert the body function."""

def true_fn(control_inputs, body_pfor, body_output, stacked):
    """Converts the body function for all but last iteration.

      This essentially converts body_output. Additionally, it needs to handle
      any control dependencies on the NextIteration node. So it creates another
      Identity node with the converted dependencies.
      """
    converted_control_inp = []
    for x in control_inputs:
        for t in x.outputs:
            converted_control_inp.append(body_pfor._convert_helper(t).t)
    if stacked:
        # Note convert always does the stacking.
        output = body_pfor.convert(body_output)
    else:
        output, convert_stacked, _ = body_pfor._convert_helper(body_output)
        assert convert_stacked == stacked, body_output
    with ops.control_dependencies(converted_control_inp):
        exit(array_ops.identity(output))

body_pfor = self._init_pfor(pfor_input.pfor, new_indices, cond_stacked,
                            new_inputs, inputs_stacked)
new_outputs = []

for i, (body_output,
        stacked) in enumerate(zip(self._body_outputs, inputs_stacked)):
    control_inp = self._next_iter_control_inputs[i]
    out_dtype = body_output.dtype
    # Note that we want to run the body only if not all pfor iterations are
    # done. If all are done, we return empty tensors since these values will
    # not be used. Notice that the value returned by the loop is based on
    # TensorArrays and not directly on these returned values.
    # pylint: disable=cell-var-from-loop
    new_output = control_flow_ops.cond(
        not_all_done,
        lambda: true_fn(control_inp, body_pfor, body_output, stacked),
        lambda: constant_op.constant([], dtype=out_dtype))
    # pylint: enable=cell-var-from-loop
    new_outputs.append(new_output)
exit(new_outputs)
