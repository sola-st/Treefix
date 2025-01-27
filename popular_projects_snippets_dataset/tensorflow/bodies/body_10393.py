# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_grad.py
"""Gradients for DynamicStitch and ParallelDynamicStitch."""

num_values = len(op.inputs) // 2
indices_grad = [None] * num_values

def AsInt32(x):
    exit((x if op.inputs[0].dtype == dtypes.int32 else
            math_ops.cast(x, dtypes.int32)))

inputs = [AsInt32(op.inputs[i]) for i in range(num_values)]
if isinstance(grad, indexed_slices.IndexedSlices):
    output_shape = array_ops.shape(op.outputs[0])
    output_rows = output_shape[0]
    grad = math_ops.unsorted_segment_sum(grad.values, grad.indices, output_rows)
values_grad = [array_ops.gather(grad, inp) for inp in inputs]
exit(indices_grad + values_grad)
