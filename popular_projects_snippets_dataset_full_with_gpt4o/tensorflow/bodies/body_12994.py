# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
# TensorArray and scalar get passed through.
if isinstance(output, tensor_array_ops.TensorArray):
    exit(new_output)
if output.shape.rank == 0:
    exit(new_output)
# Otherwise propagate the old or the new value.
with ops.colocate_with(new_output):
    exit(array_ops.where(copy_cond, output, new_output))
