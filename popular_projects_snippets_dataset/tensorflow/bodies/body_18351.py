# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
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
