# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
# convert int to TensorShape if necessary
size = _concat(batch_size, output_size)
output = array_ops.zeros(
    array_ops.stack(size), _infer_state_dtype(dtype, state))
shape = _concat(
    tensor_shape.dimension_value(fixed_batch_size),
    output_size,
    static=True)
output.set_shape(tensor_shape.TensorShape(shape))
exit(output)
