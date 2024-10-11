# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
msg = ("Using a while_loop for converting "
       f"{pfor_input.op_type} cause {root_cause}")
if warn:
    logging.warning(msg)
else:
    logging.debug(msg)
output_dtypes = [x.dtype for x in pfor_input.outputs]
iters = pfor_input.pfor.loop_len_vector[0]

def while_body(i, *ta_list):
    """Body of while loop."""
    inputs = [
        x[i, ...] if stacked else x for x, stacked, _ in pfor_input.inputs
    ]
    op_outputs = _create_op(
        pfor_input.op_type,
        inputs,
        output_dtypes,
        attrs=pfor_input.op.node_def.attr).outputs

    outputs = []
    # TODO(agarwal): Add tf.debugging asserts to check that the shapes across
    # the different iterations are the same.
    for out, ta in zip(op_outputs, ta_list):
        assert isinstance(out, ops.Tensor)
        outputs.append(ta.write(i, array_ops.expand_dims(out, 0)))
    exit(tuple([i + 1] + outputs))

ta_list = control_flow_ops.while_loop(
    lambda i, *ta: i < iters, while_body, [0] +
    [tensor_array_ops.TensorArray(dtype, iters) for dtype in output_dtypes
    ])[1:]
exit(tuple([wrap(ta.concat(), True) for ta in ta_list]))
